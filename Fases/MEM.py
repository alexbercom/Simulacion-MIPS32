# MEM: Memory

class MEM:
    def __init__(self, unidadProcesamiento):
        self.unidadProcesamiento = unidadProcesamiento

    def execute(self, ex_mem_reg):
        """
          - Lee/escribe memoria de datos para LW y SW.
          - Pasa los resultados a la siguiente etapa (WB).
        """
        data_in = ex_mem_reg.read()
        if not data_in:
            return None

        # Decodificación de la instrucción
        opcode = data_in['opcode']
        rd = data_in['rd']
        val_rd = data_in['val_rd']
        addr = data_in['addr_mem']

        if opcode == "LW":
            # Leer de memoria
            mem_data = self.unidadProcesamiento.memData.leer(addr)
            print(f"[MEM] LW desde addr={addr}, valor={mem_data}")
            data_in['val_rd'] = mem_data if mem_data is not None else 0
        elif opcode == "SW":
            # Escribir en memoria
            val_reg = self.unidadProcesamiento.registros.leer(rd)
            self.unidadProcesamiento.memData.escribir(addr, val_reg)
            print(f"[MEM] SW registro={rd} valor={val_reg} en addr={addr}")

        # Retornar los datos a la siguiente etapa (WB)
        return data_in

