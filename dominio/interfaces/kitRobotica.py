from ..CategoriaEquipo import CategoriaEquipo
from dataclasses import dataclass


@dataclass
class KitRobotica(CategoriaEquipo):
    plazo: int = 1
    tarifaDiaria: int = 12000

    #getters
    
    def obtener_plazo(self) -> int:
        return self.plazo
    
    def obtener_tarifa_diaria(self) -> int:
        return self.tarifaDiaria
    
    def obtener_nombre(self) -> str:
            return "Kit de Robótica"