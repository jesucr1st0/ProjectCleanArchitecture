from abc import ABC, abstractmethod


from dominio.Prestamo import Prestamo



class RepositorioPrestamo(ABC):
    @abstractmethod
    def consultarPrestamo(self, IdPrestamo: str) -> None: ...
    
    @abstractmethod
    def actualizarPrestamo(self, IdPrestamo: str, prestamo: Prestamo) -> None: ...
    
    @abstractmethod
    def guardarPrestamo(self, prestamo: Prestamo) -> None: ...
