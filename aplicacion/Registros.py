from aplicacion.puertos.NotificarEstudiante import NotificarEstudiante
from aplicacion.puertos.RepositorioPrestamo import RepositorioPrestamo
from dominio.Prestamo import Prestamo
from dominio.ServicioMultas import ServicioMultas
from aplicacion.puertos.ObtenerFecha import ObtenerFecha
from aplicacion.puertos.RepositorioEquipo import RepositorioEquipo
from aplicacion.puertos.RepositorioEstudiante import RepositorioEstudiante

class Registros:
    
    def __init__(self, repoEquipo: RepositorioEquipo, repoEstudiante: RepositorioEstudiante, repoPrestamo: RepositorioPrestamo, notificador: NotificarEstudiante):
        self.repoEquipo = repoEquipo
        self.repoEstudiante = repoEstudiante
        self.repoPrestamo = repoPrestamo
        self.notificador = notificador
        
        

    def registrarPrestamo(self, prestamo: Prestamo):
        equipo = prestamo.obtener_equipo_prestamo()
        estudiante = prestamo.obtener_estudiante_prestamo()
        
        if self.validarPrestamo(prestamo):
            equipo.actualizar_estado("PRESTADO")
            self.repoEquipo.actualizarEquipo(equipo)
            
            estudiante.actualizar_cantidad_prestamos(estudiante.cantidad_prestamos() + 1)
            self.repoEstudiante.actualizarEstudiante(estudiante)
            
            self.repoPrestamo.guardarPrestamo(prestamo)
            self.notificador.notificarPrestamo(estudiante)

            
    def validarPrestamo(self, prestamo: Prestamo):
        estudiante = prestamo.obtener_estudiante_prestamo()
        equipo = prestamo.obtener_equipo_prestamo()
        bd_estudiante = self.repoEstudiante.consultarEstudiante(estudiante.obtener_cedula())
        bd_equipo = self.repoEquipo.consultarEquipo(equipo.obtener_id_equipo())
        
        if bd_estudiante.tiene_multa() == True:  #Arreglar esto
                Exception("El estudiante tiene una multa pendiente, no puede realizar prestamos.")
        
        if bd_estudiante.cantidad_prestamos() > 2:    #Arreglar esto
                Exception("El estudiante ha llegado al limite de prestamos.")
                
        if bd_equipo.obtener_estado().upper() != "DISPONIBLE":  #Arreglar esto
                Exception("El equipo no se encuentra disponible para prestamo.")
                
        else:
            return True
        
    
    def registrarDevolucion(self, obtenerFecha: ObtenerFecha, prestamo: Prestamo):
        fecha_actual = obtenerFecha.obtenerFecha()
        equipo = prestamo.obtener_equipo_prestamo()
        
        estudiante = prestamo.obtener_estudiante_prestamo()
        fecha_limite = prestamo.obtener_fecha_limite()
        
        
        if fecha_actual > fecha_limite:
            dias = (fecha_actual - fecha_limite).days

            tarifa = equipo.obtener_categoria().obtener_tarifa_diaria()

            servicio_multas = ServicioMultas(tarifa)

            multa = servicio_multas.calcular_multa(dias)
            self.notificador.notificarMulta(estudiante, multa)
            
        else:
            equipo.actualizar_estado("DISPONIBLE")
            self.repoEquipo.actualizarEquipo(equipo)
            
            estudiante.actualizar_cantidad_prestamos(estudiante.cantidad_prestamos() - 1)
            self.repoEstudiante.actualizarEstudiante(estudiante)
            

    def registrarDaño(self, prestamo: Prestamo):
        equipo = prestamo.obtener_equipo_prestamo()
        
        equipo.actualizar_estado("EN_MANTENIMIENTO")
        self.repoEquipo.actualizarEquipo(equipo)
        
    

    
    
    
        
        
        
    