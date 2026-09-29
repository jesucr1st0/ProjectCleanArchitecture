"""Composición: el único lugar que conoce todas las capas.

Uso:  python main.py
"""
from datetime import datetime
import sqlite3
"""Para generar codigos aleatorios"""
import uuid

from aplicacion.Registros import Registros
from dominio.interfaces.portatil import Portatil
from dominio.Equipo import Equipo
from dominio.Estudiante import Estudiante
from dominio.Prestamo import Prestamo
from infraestructura.ProveedorFecha import ProveedorFecha
from infraestructura.RepositorioEquipoSQLite import RepositorioSQLite as RepositorioEquipoSQLite
from infraestructura.RepositorioEstudianteSQLite import RepositorioSQLite as RepositorioEstudianteSQLite
from infraestructura.RepositorioPrestamoSQLite import RepositorioSQLite as RepositorioPrestamoSQLite
from infraestructura.Notificador import Notificador
from aplicacion.puertos.ValidadorPrestamo import ValidadorPrestamo

conexion = sqlite3.connect("PrestacionEquipos.db")
conexion.execute(
    "CREATE TABLE IF NOT EXISTS equipos (idEquipo TEXT PRIMARY KEY, estado TEXT, categoria TEXT)"
)

conexion.execute(
    "CREATE TABLE IF NOT EXISTS estudiantes (cedula TEXT PRIMARY KEY, nombre TEXT, cantidadPrestamos INTEGER, multa BOOLEAN)"
)

conexion.execute(
    "CREATE TABLE IF NOT EXISTS prestamos (idPrestamo TEXT PRIMARY KEY, fechaPrestamo DATE, idEquipo TEXT, idEstudiante TEXT, fechaLimite DATE)"
)

casoUso1 = Registros(
    repoEquipo= RepositorioEquipoSQLite(conexion),
    repoEstudiante= RepositorioEstudianteSQLite(conexion),
    repoPrestamo= RepositorioPrestamoSQLite(conexion),
    notificador= Notificador()
)

categoria = Portatil()

equipo = Equipo(
    "EQ989",
    "disponible",
    categoria
)

# repositorioEquipo = RepositorioEquipoSQLite(conexion)
# repositorioEquipo.guardarEquipo(equipo)

estudiante = Estudiante(
    "0001",
    "Jesus",
    0,
    False
)

# repositorioEstudiante = RepositorioEstudianteSQLite(conexion)
# repositorioEstudiante.guardarEstudiante(estudiante)

prestamo = Prestamo(
    str(uuid.uuid4())[:8], #Generar ID aleatorio de 8 caracteres
    datetime(2026, 9, 20),
    equipo,
    estudiante,
    datetime(2026, 9, 20)
)

resultadoPrestamo = casoUso1.registrarPrestamo(prestamo)
# resultadoDevolucion = casoUso1.registrarDevolucion(ProveedorFecha(), prestamo)
# resultadoDaño = casoUso1.registrarDaño(prestamo)








