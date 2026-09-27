from aplicacion.puertos.RepositorioPrestamo import  RepositorioPrestamo


class RepositorioSQLite(RepositorioPrestamo):
    def __init__(self, conexion):
        self.db = conexion

    def guardarPrestamo(self, prestamo):
        self.db.execute("INSERT INTO prestamos VALUES (?, ?, ?, ?, ?)",
                        (prestamo.obtener_id_prestamo(), str(prestamo.obtener_fecha_prestamo()), prestamo.obtener_equipo_prestamo().obtener_id(), prestamo.obtener_estudiante_prestamo().obtener_id(), str(prestamo.obtener_fecha_limite())))
        self.db.commit()
    def consultarPrestamo(self, IdPrestamo, prestamo):
        cursor = self.db.execute("SELECT * FROM prestamos WHERE idPrestamo = ?", (IdPrestamo,))
        row = cursor.fetchone()
        if row:
            prestamo.idPrestamo = row[0]
            prestamo.fechaPrestamo = row[1]
            prestamo.equipo.idEquipo = row[2]
            prestamo.estudiante.cedula = row[3]
            prestamo.fechaLimite = row[4]
        return prestamo
    def actualizarPrestamo(self, IdPrestamo, prestamo):
        self.db.execute("UPDATE prestamos SET fechaPrestamo = ?, idEquipo = ?, idEstudiante = ?, fechaLimite = ? WHERE idPrestamo = ?",
                        (str(prestamo.obtener_fecha_prestamo()), prestamo.obtener_equipo_prestamo().obtener_id(), prestamo.obtener_estudiante_prestamo().obtener_id(), str(prestamo.obtener_fecha_limite()), IdPrestamo))
        self.db.commit()

    
