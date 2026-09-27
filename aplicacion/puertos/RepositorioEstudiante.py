from abc import ABC, abstractmethod
from dominio.Estudiante import Estudiante

class RepositorioEstudiante(ABC):
    @abstractmethod
    def consultarEstudiante(self,cedula: str) -> None: ...
    
    @abstractmethod
    def actualizarEstudiante(self, cedula: str, estudiante: Estudiante) -> None: ...
