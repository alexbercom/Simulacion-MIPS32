# ID: Instruction Decode

class ID:
    def __init__(self, unidadProcesamiento):
        self.unidadProcesamiento = unidadProcesamiento

    def execute(self, if_id_reg):
        """
          - Decodifica la instrucción
          - Identifica registros fuente/destino
          - Maneja detección de hazards
          - Maneja saltos (en caso de branch/jump)
        """
        data_in = if_id_reg.read()
        if data_in is None:
            return None

        # Obtener la instrucción completa
        instr = data_in['instr']
        pc = data_in['PC']

        # Separar la instrucción en tokens
        partes = instr.split()

        # Interpretar el opcode (primer token)
        opcode = partes[0].upper()

        # Analizar según el tipo de instrucción

        # Definimos variables para los operandos (valores por defecto None)
        rd, rs, rt, inm = None, None, None, None

        # R-Type => ADD, SUB, AND, OR, XOR, SLT, NOR
        if opcode in ["ADD", "SUB", "AND", "OR", "XOR", "SLT", "NOR"]:
            # Formato: OPCODE rd rs rt
            if len(partes) == 4:
                rd = partes[1]
                rs = partes[2]
                rt = partes[3]
        # Instrucciones de acceso a memoria
        elif opcode in ["LW", "SW"]:
            # Asumimos formato: OPCODE rd offset(base)
            # Ej: LW t1 0(t2)
            if len(partes) == 3:
                rd = partes[1]
                offset, base_reg = self._parseAddress(partes[2])
                inm = offset
                rs = base_reg
        # Instrucciones de salto condicional
        elif opcode in ["BEQ", "BNE"]:
            if len(partes) == 4:
                rs = partes[1]
                rt = partes[2]
                inm = int(partes[3])
        # Salto incondicional
        elif opcode == "J":
            if len(partes) == 2:
                inm = int(partes[1])
        else:
            # Si no encaja en los casos anteriores, se marca como desconocida
            print(f"[ID] Instruccion '{instr}' desconocida o formato no manejado.")

        # Construir la salida
        data_out = {
            'opcode': opcode,
            'rd': rd,
            'rs': rs,
            'rt': rt,
            'inm': inm,
            'pc': pc
        }

        print(f"[ID] Decodifica: {instr} => {data_out}")
        return data_out

    # Parsea algo como '8(t1)' -> (8, 't1')
    def _parseAddress(self, addr_str):
        addr_str = addr_str.replace(")", "")
        offset, reg = addr_str.split("(")
        return int(offset), reg

