from Modelo.Categoria import Categoria
from Modelo.Marca import Marca


class Producto:
    id: int
    nombre: str
    precio: float
    stock: int
    categoria: int
    marca: int

    def __init__(self, id: int, nombre: str, precio: float, stock: int, categoria: int, marca: int) -> None:
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
        self.marca = marca
        
    def __str__(self) -> str:
        return self.nombre
