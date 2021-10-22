class Cliente:
    id: int
    email: str
    nombre: str
    apellido: str
    telefono: str

    def __init__(self, id: int, email: str, nombre: str, apellido: str, telefono: str) -> None:
        self.id = id
        self.email = email
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} {self.apellido} / {self.email}"
