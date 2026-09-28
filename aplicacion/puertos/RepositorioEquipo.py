from abc import ABC, abstractmethod
from dominio.Equipo import Equipo


class RepositorioEquipo(ABC):
    
    @abstractmethod
    def guardarEquipo(self, equipo: Equipo) -> None: ...

    @abstractmethod
    def consultarEquipo(self, IdEquipo: str) -> Equipo: ...

    @abstractmethod
    def actualizarEquipo(self, idEquipo: str, equipo: Equipo) -> Equipo: ...
