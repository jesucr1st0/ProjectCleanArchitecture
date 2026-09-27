"""Composición: el único lugar que conoce todas las capas.

Uso:  python main.py
"""
import sqlite3
"""Para generar codigos aleatorios"""
import uuid
"""gestionar decimales --> Para representar dinero con exactitud."""
from decimal import Decimal

from aplicacion.Registros import RegistrarPrestamo
from aplicacion.Registros import RegistrarDevolucion
from aplicacion.puertos.NotificarEstudiante import NotificarEstudiante
from aplicacion.puertos.ObtenerFecha import ObtenerFecha
from aplicacion.puertos.RepositorioEquipo import RepositorioEquipo
from aplicacion.puertos.RepositorioEstudiante import RepositorioEstudiante
from aplicacion.puertos.RepositorioPrestamo import RepositorioPrestamo
from dominio.CategoriaEquipo import CategoriaEquipo
from dominio.Equipo import Equipo
from dominio.Estudiante import Estudiante
from dominio.Prestamo import Prestamo
from dominio.ServicioMultas import ServicioMultas
from infraestructura.ProveedorFecha import ProveedorFecha
from infraestructura.RepositorioEquipoSQLite import RepositorioSQLite as RepositorioEquipoSQLite
from infraestructura.RepositorioEstudianteSQLite import RepositorioSQLite as RepositorioEstudianteSQLite
from infraestructura.RepositorioPrestamoSQLite import RepositorioSQLite as RepositorioPrestamoSQLite
from infraestructura.Notificador import Notificador

conexion = sqlite3.connect("PrestacionEquipos.db")
conexion.execute(
    "CREATE TABLE IF NOT EXISTS equipos (idEquipo TEXT PRIMARY KEY, estado TEXT, categoria TEXT)",
    "CREATE TABLE IF NOT EXISTS estudiantes (cedula TEXT PRIMARY KEY, nombre TEXT, correo TEXT, carrera TEXT)",
    "CREATE TABLE IF NOT EXISTS prestamos (idPrestamo TEXT PRIMARY KEY, fechaPrestamo TEXT, idEquipo TEXT, idEstudiante TEXT, fechaLimite TEXT)"
)

"""Realizar pedido resibe la conexion a la db y la pasarela de pagos, y se encarga de ejecutar el caso de uso."""
caso_usoP = RegistrarPrestamo(
    """repo=RepositorioSQLite(conexion),
    pagos=PasarelaSimulada(),"""
)
caso_usoD = RegistrarDevolucion(
    """repo=RepositorioSQLite(conexion),
    pagos=PasarelaSimulada(),"""
)