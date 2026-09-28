from ..CategoriaEquipo import CategoriaEquipo
from dataclasses import dataclass


@dataclass
class Portatil(CategoriaEquipo):
    plazo: int = 3
    tarifaDiaria: int = 5000
    #getters
    
    def obtener_plazo(self) -> int:
        return self.plazo
    
    def obtener_tarifa_diaria(self) -> int:
        return self.tarifaDiaria

    def obtener_nombre(self) -> str:
        return "Portátil"