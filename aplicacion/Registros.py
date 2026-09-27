from puertos import NotificarEstudiante
from puertos import RepositorioPrestamo
from dominio import Prestamo
from dominio import ServicioMultas
from puertos import ObtenerFecha

def registrarPrestamo(fechaPrestamo, fechaLimite, cedula):
    equipo = Prestamo.obtener_equipo_prestamo()
    estudiante = Prestamo.obtener_estudiante_prestamo()
    
    if estudiante.tiene_Multa() == True:
        NotificarEstudiante.notificarMulta()
    
    if estudiante.cantidad_prestamos() > 2:
        
    
    if equipo.obtener_estado() == "disponible":
        
    