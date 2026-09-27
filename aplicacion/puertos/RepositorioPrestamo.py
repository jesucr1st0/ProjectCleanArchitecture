from abc import ABC, abstractmethod


from dominio.Prestamo import Prestamo



class RepositorioPrestamo(ABC):
    @abstractmethod
    def consultarPrestamo(self, IdPrestamo: int, prestamo: Prestamo) -> None: ...
    @abstractmethod
    def actualizarPrestamo(self, IdPrestamo: int, prestamo: Prestamo) -> None: ...
    @abstractmethod
    def guardarPrestamo(self, prestamo: Prestamo) -> None: ...
