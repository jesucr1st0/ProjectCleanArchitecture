from aplicacion.puertos.RepositorioEstudiante import RepositorioEstudiante
from aplicacion.puertos.RepositorioEquipo import RepositorioEquipo
from dominio.Prestamo import Prestamo

class ValidadorPrestamo:
    
    def validarPrestamo(prestamo: Prestamo, repoEstudiante: RepositorioEstudiante, repoEquipo: RepositorioEquipo):
        estudiante = prestamo.obtener_estudiante_prestamo()
        equipo = prestamo.obtener_equipo_prestamo()
        repoEstudiante.consultarEstudiante(estudiante.obtener_cedula())
        repoEquipo.consultarEquipo(equipo.obtener_id_equipo())
        
        if estudiante.tiene_multa() == True:  
                raise Exception("El estudiante tiene una multa pendiente, no puede realizar prestamos.")
        
        if estudiante.cantidad_prestamos() >= 2:    
                raise Exception("El estudiante ha llegado al limite de prestamos.")
                
        if equipo.obtener_estado().upper() != "DISPONIBLE": 
                raise Exception("El equipo no se encuentra disponible para prestamo.")
                
        else:
            return True