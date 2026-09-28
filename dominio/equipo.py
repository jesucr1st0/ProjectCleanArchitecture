from dataclasses import dataclass
from dominio.CategoriaEquipo import CategoriaEquipo


@dataclass
class Equipo:
    idEquipo: str
    estado: str
    categoria: CategoriaEquipo
    
    #Getters
    def obtener_id_equipo(self)-> str:
        return self.idEquipo
    
    def obtener_estado(self)-> str:
        return self.estado
    
    def obtener_categoria(self)-> CategoriaEquipo:
        return self.categoria
    
    #Setters
    def actualizar_estado(self, estado: str):
        self.estado = estado