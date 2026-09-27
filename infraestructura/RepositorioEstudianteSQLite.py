
from aplicacion.puertos.RepositorioEstudiante import RepositorioEstudiante
from dominio.Estudiante import Estudiante



class RepositorioSQLite(RepositorioEstudiante):
    def __init__(self, conexion):
        self.db = conexion

    def guardarEstudiante(self, estudiante):
        self.db.execute("INSERT INTO estudiantes VALUES (?, ?, ?, ?)",
                        (estudiante.obtener_id(), estudiante.obtener_nombre(), estudiante.obtener_correo(), estudiante.obtener_carrera()))
        self.db.commit()

    def consultarEstudiante(self, cedula):
        cursor = self.db.execute("SELECT * FROM estudiantes WHERE cedula = ?", (cedula,))
        row = cursor.fetchone()
        if row:
            estudiante = Estudiante(row[0], row[1], row[2], row[3])
            return estudiante
        return None
    
    def actualizarEstudiante(self, estudiante):
        self.db.execute("UPDATE estudiantes SET nombre = ?, correo = ?, carrera = ? WHERE cedula = ?",
                        (estudiante.obtener_nombre(), estudiante.obtener_correo(), estudiante.obtener_carrera(), estudiante.obtener_id()))
        self.db.commit()    