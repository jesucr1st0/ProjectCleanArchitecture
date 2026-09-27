from abc import ABC, abstractmethod

from dominio.Estudiante import Estudiante



class NotificarEstudiante(ABC):
    @abstractmethod
    def notificarPrestamo(self, estudiante: Estudiante, mensaje: str) -> None: ...
    @abstractmethod
    def notificarMulta(self, estudiante: Estudiante, mensaje: str) -> None: ...
