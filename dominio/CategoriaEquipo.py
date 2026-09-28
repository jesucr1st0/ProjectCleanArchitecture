from abc import ABC,abstractmethod
from dataclasses import dataclass
import datetime


@dataclass
class CategoriaEquipo(ABC):
    plazo:int
    tarifaDiaria: int
    
    #getters
    
    @abstractmethod
    def obtener_plazo(self) -> int:
        raise NotImplementedError
    
    
    @abstractmethod
    def obtener_tarifa_diaria(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def obtener_nombre(self) -> str:
        raise NotImplementedError
        
    