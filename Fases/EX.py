# EX: Execute

class EX:
    def __init__(self, unidadProcesamiento):
        self.unidadProcesamiento = unidadProcesamiento

    def execute(self, id_ex_reg):
        """
          - Realiza operaciones aritmético-lógicas (ADD, SUB, AND, OR, XOR, SLT, NOR)
          - Calcula direcciones para LW/SW
          - Verifica condiciones de salto en BEQ/BNE
          - Manejo de saltos incondicionales (J).
        """
        data_in = id_ex_reg.read()
        if data_in is None:
            return None

        # Decodificación de la instrucción
        opcode = data_in['opcode']
        rd = data_in['rd']
        rs = data_in['rs']
        rt = data_in['rt']
        inm = data_in['inm']
        pc = data_in['pc']

        # Valores por defecto
        alu_result = None
        branch_taken = False
        next_pc = pc + 4

        # Leer valores de los registros fuente
        val_rs = self.unidadProcesamiento.registros.leer(rs) if rs else 0
        val_rt = self.unidadProcesamiento.registros.leer(rt) if rt else 0

        # Decodificación y ejecución según el opcode
        if opcode == "ADD":
            alu_result = self.unidadProcesamiento.ALU.sumar(val_rs, val_rt)
        elif opcode == "SUB":
            alu_result = self.unidadProcesamiento.ALU.restar(val_rs, val_rt)
        elif opcode == "AND":
            alu_result = self.unidadProcesamiento.ALU.and_bit(val_rs, val_rt)
        elif opcode == "OR":
            alu_result = self.unidadProcesamiento.ALU.or_bit(val_rs, val_rt)
        elif opcode == "XOR":
            alu_result = self.unidadProcesamiento.ALU.xor_bit(val_rs, val_rt)
        elif opcode == "SLT":
            alu_result = self.unidadProcesamiento.ALU.slt(val_rs, val_rt)
        elif opcode == "NOR":
            alu_result = self.unidadProcesamiento.ALU.nor_bit(val_rs, val_rt)
        elif opcode == "LW" or opcode == "SW":
            # LW/SW: Cálculo de dirección de memoria (base + offset)
            alu_result = val_rs + inm
        elif opcode == "BEQ":
            # BEQ: Salto condicional si val_rs == val_rt
            if self.unidadProcesamiento.ALU.beq(val_rs, val_rt):
                branch_taken = True
                next_pc = pc + inm
        elif opcode == "BNE":
            # BNE: Salto condicional si val_rs != val_rt
            if self.unidadProcesamiento.ALU.bne(val_rs, val_rt):
                branch_taken = True
                next_pc = pc + inm
        elif opcode == "J":
            # J: Salto incondicional
            branch_taken = True
            next_pc = inm

        # Si es un branch tomado, actualizamos PC
        if branch_taken:
            self.unidadProcesamiento.PC.escribir(next_pc)
            print(f"[EX] Salto tomado a {next_pc}. PC modificado.")
        else:
            # Si no hay salto, no modificamos el PC aquí
            pass

        # Preparar los datos de salida para la siguiente etapa
        data_out = {
            'opcode': opcode,
            'rd': rd,
            'val_rd': alu_result,           # Valor que WB podría escribir
            'addr_mem': alu_result,         # Dirección de memoria (LW/SW)
            'branch_taken': branch_taken    # Indica si se tomó un salto
        }

        print(f"[EX] Ejecuta '{opcode}' => alu_result={alu_result}, branch_taken={branch_taken}")
        return data_out
