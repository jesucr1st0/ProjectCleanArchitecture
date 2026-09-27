from abc import ABC, abstractmethod

from dominio.Equipo import Equipo


class RepositorioEquipo(ABC):
    @abstractmethod
    def consultarEquipo(self, idEquipo: str) -> None: ...
    
    @abstractmethod
    def actualizarEquipo(self, idEquipo: str, equipo: Equipo) -> None: ...
