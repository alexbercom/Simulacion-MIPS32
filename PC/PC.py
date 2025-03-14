# PC: Program Counter

class PC:
    def __init__(self):
        self.valor = 0

    def leer(self):
        return self.valor

    def escribir(self, nuevo_valor):
        self.valor = nuevo_valor
