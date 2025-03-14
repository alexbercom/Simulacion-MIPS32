# Representan los registros de la CPU.

class Registros:
    def __init__(self):
        # Inicialización de los registros como un diccionario
        self.registros = {
            "zero": 0,
            "t0": 0, "t1": 0, "t2": 0, "t3": 0, "t4": 0,
            "t5": 0, "t6": 0, "t7": 0, "t8": 0, "t9": 0,
            "s0": 0, "s1": 0, "s2": 0, "s3": 0, "s4": 0,
        }

    def leer(self, reg):
        # Retorna el valor almacenado en un registro
        if reg is None:
            return 0
        return self.registros.get(reg, 0)

    def escribir(self, reg, valor):
        # Escribe un valor en un registro
        if reg == "zero":
            return      # Registro "zero" no puede ser modificado
        if reg in self.registros:
            self.registros[reg] = valor

    def mostrar_registros(self):
        # Muestra el estado actual de todos los registros
        print("[Registros] Estado final:")
        for k, v in sorted(self.registros.items()):
            print(f"  {k} = {v}")
