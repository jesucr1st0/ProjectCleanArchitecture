from dataclasses import dataclass
from datetime import datetime, timedelta

from dominio.Equipo import Equipo
from dominio.Estudiante import Estudiante


@dataclass
class Prestamo:
    idPrestamo: str
    fechaPrestamo: datetime
    equipo: Equipo
    estudiante: Estudiante
    fechaLimite: datetime
            
    
    #Getters
    
    def obtener_id_prestamo(self) -> str:
        return self.idPrestamo
    
    def obtener_fecha_prestamo(self) -> datetime:
        return self.fechaPrestamo
    
    def obtener_equipo_prestamo(self) -> Equipo:
        return self.equipo
    
    def obtener_estudiante_prestamo(self) -> Estudiante:
        return self.estudiante
    
    def obtener_fecha_limite(self) -> datetime: 
        return self.fechaLimite + timedelta(days=self.equipo.obtener_categoria().obtener_plazo())

