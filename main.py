from CPU.CPU import CPU

def main():
    # Crear la CPU
    cpu = CPU()

    # Cargar las instrucciones desde un fichero de texto
    cpu.loadInstrucciones("instrucciones.txt")

    # Cargar los datos iniciales en memoria desde un fichero de texto
    cpu.loadData("datos.txt")

    # Inicializar y arrancar la segmentación
    cpu.unidadControl.initSegmentation()

    # Mostrar estado final de la CPU
    print("\n===== EJECUCIÓN FINALIZADA =====")
    cpu.unidadProcesamiento.registros.mostrar_registros()

    # Mostrar el contenido de la memoria de datos
    cpu.unidadProcesamiento.memData.mostrar_memoria()

if __name__ == "__main__":
    main()
