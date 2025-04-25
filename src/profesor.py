from src.persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, dni, sueldo):
        super().__init__(nombre, apellido, dni)
        if sueldo < 0:
            raise ValueError("El sueldo no puede ser negativo")
        self.sueldo = sueldo

    def __repr__(self):
        return f"Profesor: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Sueldo: {self.sueldo}"
