from dataclasses import dataclass

@dataclass
class Estudiante:
    cedula: str
    nombre: str
    cantidadPrestamos: int
    multa: bool
    
    #Getters
    def obtener_cedula(self) -> str:
        return self.cedula
    
    def obtener_nombre(self) -> str:
        return self.nombre
    
    def cantidad_prestamos(self) -> int:
        return self.cantidadPrestamos
    
    def tiene_multa(self) -> bool:
        return self.multa
    
    #Setters
    def actualizar_cantidad_prestamos(self, cantidad: int) -> None:
        self.cantidadPrestamos = cantidad
    
    def actualizar_multa(self, multa: bool) -> None:
        self.multa = multa
    
    