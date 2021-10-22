class ModoPago:
    id: int
    nombre: str
    detalles: str

    def __init__(self, id: int, nombre: str, detalles: str) -> None:
        self.id = id
        self.detalles = detalles.capitalize()
        self.nombre = nombre.capitalize()

    def __str__(self) -> str:
        return self.nombre
