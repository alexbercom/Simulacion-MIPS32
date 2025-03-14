# WB: Write Back

class WB:
    def __init__(self, unidadProcesamiento):
        self.unidadProcesamiento = unidadProcesamiento

    def execute(self, mem_wb_reg):
        # Escribe el resultado final en el registro destino si corresponde.
        data_in = mem_wb_reg.read()
        if not data_in:
            return

        # Decodificación de la instrucción
        opcode = data_in['opcode']
        rd = data_in['rd']
        val_rd = data_in.get('val_rd', None)

        # Escribir en el registro si la instrucción lo requiere
        if opcode in ["ADD", "SUB", "AND", "OR", "XOR", "SLT", "NOR", "LW"]:
            if rd and val_rd is not None:
                print(f"[WB] Escribe en {rd} el valor {val_rd}")
                self.unidadProcesamiento.registros.escribir(rd, val_rd)

        # Instrucciones como SW, BEQ, J no escriben en registros.