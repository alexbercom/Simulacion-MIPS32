# Realiza operaciones aritméticas y lógicas.

class ALU:
    def sumar(self, a, b): return a + b
    def restar(self, a, b): return a - b
    def and_bit(self, a, b): return a & b
    def or_bit(self, a, b): return a | b
    def xor_bit(self, a, b): return a ^ b
    def slt(self, a, b): return 1 if a < b else 0
    def nor_bit(self, a, b): return ~(a | b)
    def beq(self, a, b): return a == b
    def bne(self, a, b): return a != b

