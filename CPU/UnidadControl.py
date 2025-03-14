# Clase que representa la Unidad de Control

from CPU.Segmentacion import Segmentacion

class UnidadControl:
    def __init__(self, unidadProcesamiento):
        self.unidadProcesamiento = unidadProcesamiento
        self.segmentation = Segmentacion(self.unidadProcesamiento)

    def initSegmentation(self):
        self.segmentation.initSegmentation()
