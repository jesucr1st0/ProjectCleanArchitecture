from ..CategoriaEquipo import CategoriaEquipo
from dataclasses import dataclass


@dataclass
class Camara(CategoriaEquipo):
    plazo: int = 2
    tarifaDiaria: int = 8000

    #getters
    
    def obtener_plazo(self) -> int:
        return self.plazo
    
    def obtener_tarifa_diaria(self) -> int:
        return self.tarifaDiaria
    
    def obtener_nombre(self) -> str:
            return "Cámara"