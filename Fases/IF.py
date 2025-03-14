# IF: Instruction Fetch

class IF:
    def __init__(self, unidadProcesamiento):
        self.unidadProcesamiento = unidadProcesamiento

    def execute(self):
        # Lee la instrucción en PC
        pc_actual = self.unidadProcesamiento.PC.leer()
        instruccion = self.unidadProcesamiento.memIns.leer(pc_actual)

        if instruccion is None:
            print(f"[IF] No hay instruccion en PC={pc_actual}.")
            return None

        # Incrementar PC en 4
        self.unidadProcesamiento.PC.escribir(pc_actual + 4)

        print(f"[IF] Lee instruccion '{instruccion}' en PC={pc_actual}. PC -> {pc_actual + 4}")
        return {
            'PC': pc_actual,
            'instr': instruccion
        }
