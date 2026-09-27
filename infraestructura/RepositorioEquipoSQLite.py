
from aplicacion.puertos.RepositorioEquipo import RepositorioEquipo



class RepositorioSQLite(RepositorioEquipo):
    def __init__(self, conexion):
        self.db = conexion

    def guardarEquipo(self, equipo):
        self.db.execute("INSERT INTO equipos VALUES (?, ?, ?, ?)",
                        (equipo.obtener_id(), equipo.obtener_nombre(), equipo.obtener_descripcion(), equipo.obtener_disponible()))
        self.db.commit()

    def consultarEquipo(self, IdEquipo, equipo):
        cursor = self.db.execute("SELECT * FROM equipos WHERE idEquipo = ?", (IdEquipo,))
        row = cursor.fetchone()
        if row:
            equipo.idEquipo = row[0]
            equipo.estado = row[1]
            equipo.categoria = row[2]
        return equipo
    
    def actualizarEquipo(self, IdEquipo, equipo):
        self.db.execute("UPDATE equipos SET estado = ?, categoria = ? WHERE idEquipo = ?",
                        (equipo.obtener_estado(), equipo.obtener_categoria(), IdEquipo))
        self.db.commit()