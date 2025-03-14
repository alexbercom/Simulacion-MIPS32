# Controla la ejecución general, administra el pipeline y la interacción entre sus componentes

from CPU.UnidadControl import UnidadControl
from CPU.UnidadProcesamiento import UnidadProcesamiento

class CPU:
    def __init__(self):
        # La CPU tiene una unidad de procesamiento y una unidad de control
        self.unidadProcesamiento = UnidadProcesamiento()
        self.unidadControl = UnidadControl(self.unidadProcesamiento)

    def loadInstrucciones(self, txt):
        # Lee un fichero de texto con instrucciones y las carga en la memoria de instrucciones
        try:
            with open(txt, 'r') as f:
                lines = f.readlines()
                addr = 0
                for line in lines:
                    # Elimina espacios en blanco al inicio y fin
                    line = line.strip()

                    # Ignora las líneas vacías o que comiencen con '#'
                    if not line or line.startswith('#'):
                        continue

                    # Elimina la parte del comentario parcial (si lo hubiese)
                    instr_no_comment = line.split('#')[0].strip()

                    # Si tras eliminar el comentario parcial sigue habiendo texto:
                    if instr_no_comment:
                        # Se guarda la instrucción en la memoria de instrucciones
                        self.unidadProcesamiento.memIns.escribir(addr, instr_no_comment)
                        addr += 4   # Avanza la dirección de instrucción
        except FileNotFoundError:
            print(f"ERROR: No se encuentra el fichero {txt}.")

    def loadData(self, txt):
        # Cargar datos iniciales en la memoria de datos desde txt
        try:
            with open(txt, 'r') as f:
                # Ejemplo de lectura de datos
                for line in f:
                    line = line.strip()
                    if line:
                        dir_str, val_str = line.split()
                        dir_int = int(dir_str)
                        val_int = int(val_str)
                        self.unidadProcesamiento.memData.escribir(dir_int, val_int)
        except FileNotFoundError:
            print(f"ERROR: No se encuentra el fichero {txt}.")
