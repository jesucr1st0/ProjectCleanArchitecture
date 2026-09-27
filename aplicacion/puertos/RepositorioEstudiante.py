from abc import ABC, abstractmethod
from dominio.Estudiante import Estudiante

class RepositorioEstudiante(ABC):
    @abstractmethod
    def consultarEstudiante(self,IdEstudiante: int, estudiante: Estudiante) -> None: ...
    @abstractmethod
    def actualizarEstudiante(self, IdEstudiante: int, estudiante: Estudiante) -> None: ...
