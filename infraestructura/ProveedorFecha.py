
import datetime

from aplicacion.puertos.ObtenerFecha import ObtenerFecha


class ProveedorFecha(ObtenerFecha):
    def obtenerFecha(self) -> datetime:
        return datetime.now()
        
