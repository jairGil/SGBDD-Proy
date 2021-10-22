class Marca:
    id: int
    nombre: str

    def __init__(self, id: int, nombre: str) -> None:
        self.id = id
        self.nombre = nombre

    def __str__(self) -> str:
        return self.nombre
