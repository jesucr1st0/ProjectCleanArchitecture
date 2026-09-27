from abc import ABC, abstractmethod
from dominio.Equipo import Equipo

class RepositorioEquipo(ABC):

    @abstractmethod
    def consultarEquipo(self, IdEquipo: str) -> Equipo: ...

    @abstractmethod
    def actualizarEquipo(self, equipo: Equipo) -> None: ...
