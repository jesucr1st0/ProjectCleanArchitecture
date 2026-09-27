from dataclasses import dataclass, field
import datetime

from dominio.Equipo import Equipo
from dominio.Estudiante import Estudiante


@dataclass
class Prestamo:
    idPrestamo: str
    fechaPrestamo: datetime
    equipo: Equipo
    estudiante: Estudiante
    fechaLimite: datetime

    def equpo_prestamo(self) -> Equipo:
        return self.equipo

    def estudiante_prestamo(self) -> Estudiante:
        return self.estudiante
