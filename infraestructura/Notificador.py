
import datetime

from aplicacion.puertos.NotificarEstudiante import NotificarEstudiante


class Notificador(NotificarEstudiante):
    def notificarPrestamo(self, estudiante):
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"Notificación de préstamo para {estudiante.obtener_nombre()} ({estudiante.obtener_cedula()}): {"El prestamo fue exitoso"} - Fecha: {fecha_actual}"

    def notificarMulta(self, estudiante, multa: int):
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"Notificación de multa para {estudiante.obtener_nombre()} ({estudiante.obtener_cedula()}): {"Tiene una multa pendiente con un monto de $" + str(multa) } - Fecha: {fecha_actual}"
        
