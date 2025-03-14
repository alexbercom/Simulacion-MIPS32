# 🖥️ Simulador de Segmentación MIPS 🖥️

## 📌 Descripción
Este proyecto implementa un **simulador de segmentación MIPS** en Python, replicando el funcionamiento de un **pipeline de cinco etapas**. El objetivo principal es ilustrar el flujo de ejecución de instrucciones en una arquitectura segmentada, permitiendo visualizar cómo las instrucciones avanzan a través de las etapas del pipeline en cada ciclo de reloj.

El programa es capaz de manejar instrucciones **aritmético-lógicas**, **acceso a memoria** y **saltos condicionales/incondicionales**. Además, incluye detección de **hazards de datos (RAW - Read After Write)**, aplicando *stalls* cuando una instrucción necesita un resultado que aún no ha sido escrito.

El simulador sigue el modelo de **cinco etapas** del pipeline MIPS:
1. **IF (Instruction Fetch)**: Obtención de la instrucción desde la memoria.
2. **ID (Instruction Decode)**: Decodificación e identificación de operandos.
3. **EX (Execute)**: Cálculo en la ALU o dirección de memoria.
4. **MEM (Memory Access)**: Acceso a memoria para carga o almacenamiento.
5. **WB (Write Back)**: Escritura de resultados en los registros.

## 🛠️ Tecnologías utilizadas
- **Python 3.x** (Lenguaje principal).
- **Programación Orientada a Objetos (POO)** para modularidad.
- **Simulación de pipeline** basada en registros de acoplamiento.
- **Detección de RAW hazards** con aplicación de *stalls*.
- **Estructuras de datos** para modelar registros y memoria.

## 📥 Instalación
### 1️⃣ Requisitos previos
Asegúrate de tener Python 3.8 o superior instalado en tu sistema. Puedes comprobar tu versión con:
```bash
python --version
```

### 2️⃣ Clonar el repositorio
Clona el repositorio en tu máquina local con:
```bash
git clone https://github.com/tu-repo/simulador-mips-pipeline.git
cd simulador-mips-pipeline
```

## ▶️ Ejecución del programa
Para ejecutar la simulación, simplemente ejecuta el archivo main.py.

El programa cargará instrucciones y datos iniciales desde archivos de texto y simulará la ejecución del pipeline MIPS, mostrando el avance de cada instrucción en la consola.

## 🏗️ Estructura del Proyecto
```bash
.
├── ALU/      
│   ├── ALU.py                  # Implementación de la ALU (suma, resta, AND, OR, etc.)
├── CPU/                        # Componentes principales del procesador
│   ├── CPU.py                  # Clase principal de la CPU
│   ├── UnidadControl.py        # Control del pipeline
│   ├── UnidadProcesamiento.py  # Procesamiento del pipeline
│   └── Segmentacion.py         # Gestión del flujo segmentado
├── Fases/                      # Clases para las fases del pipeline
│   ├── IF.py                   # Instruction Fetch
│   ├── ID.py                   # Instruction Decode
│   ├── EX.py                   # Execute
│   ├── MEM.py                  # Memory Access
│   └── WB.py                   # Write Back
├── Memoria/                    # Memorias y registros
│   ├── Memoria.py              # Clase base de memoria
│   ├── MemoriaDatos.py         # Memoria de datos
│   ├── MemoriaInstrucciones.py # Memoria de instrucciones
│   └── Registros.py            # Banco de registros
├── RegistrosAcoplamiento/      # Registros intermedios del pipeline
│   ├── IF_ID.py
│   ├── ID_EX.py
│   ├── EX_MEM.py
│   └── MEM_WB.py
├── PC/     
│   ├── PC.py                   # Program Counter
├── instrucciones.txt           # Instrucciones de entrada
├── datos.txt                   # Datos iniciales en memoria (opcional)
└── main.py                     # Punto de entrada del programa
```

## ⚙️ Funcionamiento del Programa
1. Carga de Instrucciones y Datos
   - Se leen las instrucciones desde instrucciones.txt.
   - Opcionalmente, se cargan datos en memoria desde datos.txt.
   - Se almacenan en la memoria de instrucciones y datos, respectivamente.

2. Ejecución del Pipeline
   - Se inicia el pipeline y se procesan las instrucciones en ciclos de reloj.
   - Cada instrucción avanza por las fases IF → ID → EX → MEM → WB.
   - Se imprimen mensajes en consola mostrando el estado de cada etapa.

3. Manejo de Saltos y Peligros de Datos
   - Se actualiza el PC correctamente cuando se detecta un salto (BEQ, BNE, J).
   - Se detectan hazards RAW y se aplican stalls cuando es necesario.

4. Finalización y Resultados
   - El simulador se detiene cuando no quedan instrucciones en el pipeline.
   - Se imprime el estado final de los registros y la memoria.

## 📜 Entrada y Salida
El fichero instrucciones.txt es el fichero que contiene las instrucciones que se van a ejecutar en el programa, este contiene unas instrucciones predefinidas pero este se puede modificar o incluso poner un nuevo fichero como entrada. 

Lo mismo ocurre con datos.txt, solo que este contiene el valor de los datos que se cargaran en memoria.

La dalida del programa contendrá las fases que se ejecutan en cada uno de los ciclo, y al finalizar la ejecución mostrará los valores de las variables de los registros y la memoria.

## 📝 Reglas del Pipeline
- Cada instrucción tarda 5 ciclos en completarse.
- Se permite la ejecución en paralelo de diferentes fases en el pipeline.
- Los *stalls* se activan cuando una instrucción necesita un registro aún no escrito (hazard RAW).
- Si se detecta un salto (BEQ, BNE, J), el PC se actualiza correctamente.

## 👨‍💻 Autor
Alex Bermejo Compán
