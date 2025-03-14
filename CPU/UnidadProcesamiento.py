# Gestiona el estado de los registros, memoria y el contador del programa (PC).

from Memoria.MemoriaInstrucciones import MemoriaInstrucciones
from Memoria.MemoriaDatos import MemoriaDatos
from Memoria.Registros import Registros
from ALU.ALU import ALU
from PC.PC import PC

class UnidadProcesamiento:
    def __init__(self):
        self.PC = PC()                          # Program Counter
        self.memIns = MemoriaInstrucciones()    # Memoria de instrucciones
        self.memData = MemoriaDatos()           # Memoria de datos
        self.registros = Registros()            # Banco de registros
        self.ALU = ALU()                        # ALU

