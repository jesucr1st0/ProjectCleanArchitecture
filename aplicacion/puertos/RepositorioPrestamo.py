from abc import ABC, abstractmethod
from dominio.Prestamo import Prestamo

class RepositorioPrestamo(ABC):
    @abstractmethod
    def consultarPrestamo(self, IdPrestamo: str) -> Prestamo: ...

    @abstractmethod
    def actualizarPrestamo(self, prestamo: Prestamo) -> None: ...

    @abstractmethod
    def guardarPrestamo(self, prestamo: Prestamo) -> None: ...
