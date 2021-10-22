class Categoria:
    id: int
    nombre: str
    descripcion: str

    def __init__(self, id: int, nombre: str, descripcion: str) -> None:
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self) -> str:
        return self.nombre
