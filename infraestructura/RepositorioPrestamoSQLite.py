from aplicacion.puertos.RepositorioPrestamo import  RepositorioPrestamo

from dominio.Equipo import Equipo
from dominio.Estudiante import Estudiante
from dominio.Prestamo import Prestamo

from datetime import datetime
class RepositorioSQLite(RepositorioPrestamo):
    def __init__(self, conexion):
        self.db = conexion

    def guardarPrestamo(self, prestamo):
        self.db.execute("INSERT INTO prestamos VALUES (?, ?, ?, ?, ?)",
                        (prestamo.obtener_id_prestamo(), str(prestamo.obtener_fecha_prestamo()), prestamo.obtener_equipo_prestamo().obtener_id(), prestamo.obtener_estudiante_prestamo().obtener_id(), str(prestamo.obtener_fecha_limite())))
        self.db.commit()
    def consultarPrestamo(self, IdPrestamo):
        cursor = self.db.execute("SELECT * FROM prestamos WHERE idPrestamo = ?", (IdPrestamo,))
        row = cursor.fetchone()
        if row:
            equipo = Equipo(row[2], "", "", 0)  # Solo se necesita el ID del equipo
            estudiante = Estudiante(row[3], "", "", "")  # Solo se necesita la cédula del estudiante
            prestamo = Prestamo(row[0], datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S"), equipo, estudiante, datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S"))
            return prestamo
        return None
    def actualizarPrestamo(self, IdPrestamo, prestamo):
        self.db.execute("UPDATE prestamos SET fechaPrestamo = ?, idEquipo = ?, idEstudiante = ?, fechaLimite = ? WHERE idPrestamo = ?",
                        (str(prestamo.obtener_fecha_prestamo()), prestamo.obtener_equipo_prestamo().obtener_id(), prestamo.obtener_estudiante_prestamo().obtener_id(), str(prestamo.obtener_fecha_limite()), IdPrestamo))
        self.db.commit()

    
