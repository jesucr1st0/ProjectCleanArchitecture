from ..CategoriaEquipo import CategoriaEquipo
from dataclasses import dataclass


@dataclass
class Camara(CategoriaEquipo):
    plazo: 2
    tarifaDiaria: 8000
    
    #getters
    
    def obtener_plazo(self) -> int:
        return self.plazo
    
    def obtener_tarifa_diaria(self) -> int:
        return self.tarifaDiaria