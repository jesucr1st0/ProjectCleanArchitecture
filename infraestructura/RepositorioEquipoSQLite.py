
from aplicacion.puertos.RepositorioEquipo import RepositorioEquipo
from dominio.Equipo import Equipo
from dominio.interfaces.portatil import Portatil



class RepositorioSQLite(RepositorioEquipo):
    def __init__(self, conexion):
        self.db = conexion

    def guardarEquipo(self, equipo):
        self.db.execute("INSERT INTO equipos VALUES (?, ?, ?)",
                        (equipo.obtener_id_equipo(), equipo.obtener_estado(), equipo.obtener_categoria().obtener_nombre()))
        self.db.commit()

    def consultarEquipo(self, IdEquipo):
        cursor = self.db.execute("SELECT * FROM equipos WHERE idEquipo = ?", (IdEquipo,))
        row = cursor.fetchone()
        if row:
            equipo = Equipo(row[0], row[1], row[2])
            return equipo
        print("NO SE ENCONTRÓ EL EQUIPO")
        return None
        
    def actualizarEquipo(self, equipo):
      self.db.execute(
        "UPDATE equipos SET estado = ?, categoria = ? WHERE idEquipo = ?",
        (
            equipo.obtener_estado(),
            equipo.obtener_categoria().obtener_nombre(),
            equipo.obtener_id_equipo()
        )
    )

      self.db.commit()
