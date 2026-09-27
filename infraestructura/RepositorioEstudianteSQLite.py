
from aplicacion.puertos.RepositorioEstudiante import RepositorioEstudiante



class RepositorioSQLite(RepositorioEstudiante):
    def __init__(self, conexion):
        self.db = conexion

    def guardarEstudiante(self, estudiante):
        self.db.execute("INSERT INTO estudiantes VALUES (?, ?, ?, ?)",
                        (estudiante.obtener_id(), estudiante.obtener_nombre(), estudiante.obtener_correo(), estudiante.obtener_carrera()))
        self.db.commit()

    def consultarEstudiante(self, IdEstudiante, estudiante):
        cursor = self.db.execute("SELECT * FROM estudiantes WHERE idEstudiante = ?", (IdEstudiante,))
        row = cursor.fetchone()
        if row:
            estudiante.cedula = row[0]
            estudiante.nombre = row[1]
            estudiante.cantidadPrestamos = row[2]
            estudiante.multa = row[3]
        return estudiante
    def actualizarEstudiante(self, IdEstudiante, estudiante):
        self.db.execute("UPDATE estudiantes SET nombre = ?, cantidadPrestamos = ?, multa = ? WHERE idEstudiante = ?",
                        (estudiante.obtener_nombre(), estudiante.cantidad_prestamos(), estudiante.tiene_multa(), IdEstudiante))
        self.db.commit()