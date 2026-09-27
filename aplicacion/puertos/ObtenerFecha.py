from abc import ABC, abstractmethod
from datetime import datetime



class ObtenerFecha(ABC):
    @abstractmethod
    def obtenerFecha(self) -> datetime: ...
