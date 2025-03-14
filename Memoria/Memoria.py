# Gestionan las operaciones de carga y almacenamiento.

class Memoria:
    def __init__(self):
        self.diccionario = {}

    def leer(self, direccion):
        # Lee el contenido de una dirección de memoria
        return self.diccionario.get(direccion, None)

    def escribir(self, direccion, valor):
        # Escribe un valor en la dirección de memoria indicada
        self.diccionario[direccion] = valor

    def mostrar_memoria(self):
        # Muestra el contenido actual de la memoria, ordenado por direcciones
        print("[Memoria] Contenido:")
        for k, v in sorted(self.diccionario.items()):
            print(f"  Dir {k} => {v}")

