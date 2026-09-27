
import datetime

from aplicacion.puertos.NotificarEstudiante import NotificarEstudiante


class ProveedorFecha(NotificarEstudiante):
    def notificarPrestamo(self, estudiante, mensaje):
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"Notificación de préstamo para {estudiante.obtener_nombre()} ({estudiante.obtener_id()}): {mensaje} - Fecha: {fecha_actual}"

    def notificarMulta(self, estudiante, mensaje):
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"Notificación de multa para {estudiante.obtener_nombre()} ({estudiante.obtener_id()}): {mensaje} - Fecha: {fecha_actual}"
        
