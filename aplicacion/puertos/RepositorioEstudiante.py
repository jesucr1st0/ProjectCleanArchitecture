from abc import ABC, abstractmethod
from dominio.Estudiante import Estudiante

class RepositorioEstudiante(ABC):
    
    @abstractmethod
    def guardarEstudiante(self, estudiante: Estudiante) -> None: ...

    @abstractmethod
    def consultarEstudiante(self,cedula: str) -> Estudiante: ...

    @abstractmethod
    def actualizarEstudiante(self, estudiante: Estudiante) -> Estudiante: ...
