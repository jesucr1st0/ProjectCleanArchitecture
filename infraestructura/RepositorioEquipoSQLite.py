
from aplicacion.puertos.RepositorioEquipo import RepositorioEquipo
from dominio.Equipo import Equipo



class RepositorioSQLite(RepositorioEquipo):
    def __init__(self, conexion):
        self.db = conexion

    def guardarEquipo(self, equipo):
        self.db.execute("INSERT INTO equipos VALUES (?, ?, ?, ?)",
                        (equipo.obtener_id(), equipo.obtener_nombre(), equipo.obtener_descripcion(), equipo.obtener_disponible()))
        self.db.commit()

    def consultarEquipo(self, IdEquipo):
        cursor = self.db.execute("SELECT * FROM equipos WHERE idEquipo = ?", (IdEquipo,))
        row = cursor.fetchone()
        if row:
            equipo = Equipo(row[0], row[1], row[2], row[3])
            return equipo
        return None
    
    def actualizarEquipo(self, equipo):
        self.db.execute("UPDATE equipos SET nombre = ?, descripcion = ?, disponible = ? WHERE idEquipo = ?",
                        (equipo.obtener_nombre(), equipo.obtener_descripcion(), equipo.obtener_disponible(), equipo.obtener_id()))
        self.db.commit()