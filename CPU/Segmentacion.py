# Administra las fases del pipeline (IF, ID, EX, MEM, WB)

from Fases.IF import IF
from Fases.ID import ID
from Fases.EX import EX
from Fases.MEM import MEM
from Fases.WB import WB

from RegistrosAcoplamiento.IF_ID import IF_ID
from RegistrosAcoplamiento.ID_EX import ID_EX
from RegistrosAcoplamiento.EX_MEM import EX_MEM
from RegistrosAcoplamiento.MEM_WB import MEM_WB

class Segmentacion:
    def __init__(self, unidadProcesamiento):
        self.unidadProcesamiento = unidadProcesamiento

        # Instancias de fases
        self.IF_stage = IF(self.unidadProcesamiento)
        self.ID_stage = ID(self.unidadProcesamiento)
        self.EX_stage = EX(self.unidadProcesamiento)
        self.MEM_stage = MEM(self.unidadProcesamiento)
        self.WB_stage = WB(self.unidadProcesamiento)

        # Registros de acoplamiento
        self.IF_ID_reg = IF_ID()
        self.ID_EX_reg = ID_EX()
        self.EX_MEM_reg = EX_MEM()
        self.MEM_WB_reg = MEM_WB()

        # Señales de control de hazards
        self.stall = False
        self.finish = False

    def initSegmentation(self):
        # Bucle principal del pipeline. Se ejecuta hasta que ya no haya más instrucciones que procesar
        ciclo = 1
        while not self.finish and ciclo <= 50:
            print(f"\n===== CICLO {ciclo} =====")
            self._pipeline_cycle()
            ciclo += 1

        print("\nNo hay mas instrucciones en el pipeline. Fin de la segmentacion.")

    def _pipeline_cycle(self):
        # 1) WB
        self.WB_stage.execute(self.MEM_WB_reg)

        # 2) MEM
        ex_mem_out = self.MEM_stage.execute(self.EX_MEM_reg)
        self._actualizarAcoplamiento(self.MEM_WB_reg, ex_mem_out)

        # 3) EX
        id_ex_out = self.EX_stage.execute(self.ID_EX_reg)
        self._actualizarAcoplamiento(self.EX_MEM_reg, id_ex_out)

        # 4) ID
        # Si hay stall, no avanzamos ID -> ID_EX
        if not self.stall:
            if_id_out = self.ID_stage.execute(self.IF_ID_reg)
            self._actualizarAcoplamiento(self.ID_EX_reg, if_id_out)
        else:
            print("[INFO] Stall activo en ID. No se avanza a ID_EX.")
            self._actualizarAcoplamiento(self.ID_EX_reg, None)

        # 5) IF
        # Si hay stall, tampoco avanzamos IF
        if not self.stall:
            if_id_reg_out = self.IF_stage.execute()
            self._actualizarAcoplamiento(self.IF_ID_reg, if_id_reg_out)
            if if_id_reg_out is None:
                # Significa que no se pudo leer nueva instrucción => pipeline se vacía
                # El pipeline terminará cuando se drenen las instrucciones pendientes
                # Revisamos si las demás etapas también están vacías
                if (not self.IF_ID_reg.read() and
                    not self.ID_EX_reg.read() and
                    not self.EX_MEM_reg.read() and
                    not self.MEM_WB_reg.read()):
                    self.finish = True
        else:
            print("[INFO] Stall activo en IF. No se avanza a IF_ID.")
            self._actualizarAcoplamiento(self.IF_ID_reg, None)

    def _actualizarAcoplamiento(self, reg_acoplamiento, data):
        reg_acoplamiento.write(data)
