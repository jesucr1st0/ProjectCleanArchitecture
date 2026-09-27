from puertos import NotificarEstudiante
from puertos import RepositorioPrestamo
from dominio import Prestamo
from dominio import ServicioMultas
from puertos import ObtenerFecha
from puertos import RepositorioEquipo
from puertos import RepositorioEstudiante

class Registros:
    
    def __init__(self, repoEquipo: RepositorioEquipo, repoEstudiante: RepositorioEstudiante, repoPrestamo: RepositorioPrestamo, notificador: NotificarEstudiante, obtenerFecha: ObtenerFecha):
        self.repoEquipo = repoEquipo
        self.repoEstudiante = repoEstudiante
        self.repoPrestamo = repoPrestamo
        self.notificador = notificador
        self.obtenerFecha = obtenerFecha
        
        

    def registrarPrestamo(self, prestamo: Prestamo):
        equipo = prestamo.obtener_equipo_prestamo()
        estudiante = prestamo.obtener_estudiante_prestamo()
        
        if self.validarPrestamo(prestamo):
            equipo_actualizado = equipo.actualizar_estado("PRESTADO")
            self.repoEquipo.actualizarEquipo(equipo_actualizado)
            
            estudiante_actualizado = estudiante.actualizar_cantidad_prestamos(estudiante.cantidad_prestamos() + 1)
            self.repoEstudiante.actualizarEstudiante(estudiante_actualizado)
            
            self.repoPrestamo.guardarPrestamo(prestamo)
            self.notificador.notificarPrestamo(estudiante)

            
    def validarPrestamo(self, prestamo: Prestamo):
        estudiante = prestamo.obtener_estudiante_prestamo()
        equipo = prestamo.obtener_equipo_prestamo()
        bd_estudiante = self.repoEstudiante.consultarEstudiante(estudiante.obtener_cedula())
        bd_equipo = self.repoEquipo.consultarEquipo(equipo.obtener_id_equipo())
        
        if bd_estudiante.tiene_Multa() == True:  #Arreglar esto
                Exception("El estudiante tiene una multa pendiente, no puede realizar prestamos.")
        
        if bd_estudiante.cantidad_prestamos() > 2:    #Arreglar esto
                Exception("El estudiante ha llegado al limite de prestamos.")
                
        if bd_equipo.obtener_estado().upper() != "DISPONIBLE":  #Arreglar esto
                Exception("El equipo no se encuentra disponible para prestamo.")
                
        else:
            return True
        
        
    def registrarDevolucion(self, obtenerFecha: ObtenerFecha, prestamo: Prestamo):
        fecha_actual = obtenerFecha.obtenerFecha()
        fecha_limite = prestamo.obtener_fecha_limite()
        estudiante = prestamo.obtener_estudiante_prestamo()
        equipo = prestamo.obtener_equipo_prestamo()
        
        
        if fecha_actual > fecha_limite:
            dias = (fecha_actual - fecha_limite)
            tarifa = equipo.obtener_categoria().obtener_tarifa_diaria()
            ServicioMultas.calcular_multa(dias, tarifa)
            NotificarEstudiante.notificarMulta(estudiante)
            
        else:
            equipo_actualizado = equipo.actualizar_estado("DISPONIBLE")
            self.repoEquipo.actualizarEquipo(equipo_actualizado)
            
            estudiante_actualizado = estudiante.actualizar_cantidad_prestamos(estudiante.cantidad_prestamos() - 1)
            RepositorioEstudiante.actualizarEstudiante(estudiante_actualizado)
            

    def registrarDaño(self, prestamo: Prestamo):
        equipo = prestamo.obtener_equipo_prestamo()
        
        equipo_actualizado = equipo.actualizar_estado("EN_MANTENIMIENTO")
        self.repoEquipo.actualizarEquipo(equipo_actualizado)
        
    

    
    
    
        
        
        
    