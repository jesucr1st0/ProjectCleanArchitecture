from abc import ABC, abstractmethod

from dominio.Estudiante import Estudiante



class NotificarEstudiante(ABC):
    @abstractmethod
    def notificarPrestamo(self, estudiante: Estudiante, mensaje: str) -> str: ...
    
    @abstractmethod
    def notificarMulta(self, estudiante: Estudiante, mensaje: str) -> str: ...
