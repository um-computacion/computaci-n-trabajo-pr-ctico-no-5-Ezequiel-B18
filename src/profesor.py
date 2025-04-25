from src.persona import Persona

class Profesor(Persona):
    """Clase que representa a un profesor, hereda de Persona.
    
    Esta clase extiende la clase Persona para modelar a un profesor
    con un sueldo asociado.
    
    Attributes:
        nombre (str): Heredado de Persona.
        apellido (str): Heredado de Persona.
        dni (str): Heredado de Persona.
        pensamientos (int): Heredado de Persona.
        ultima_idea (str): Heredado de Persona.
        sueldo (float): Salario del profesor.
    """
    
    def __init__(self, nombre, apellido, dni, sueldo):
        """Inicializa una nueva instancia de Profesor.
        
        Args:
            nombre (str): Nombre del profesor.
            apellido (str): Apellido del profesor.
            dni (str): Documento Nacional de Identidad.
            sueldo (float): Salario del profesor.
            
        Raises:
            ValueError: Si el sueldo es negativo.
        """
        super().__init__(nombre, apellido, dni)
        if sueldo < 0:
            raise ValueError("El sueldo no puede ser negativo")
        self.sueldo = sueldo

    def __repr__(self):
        """Devuelve una representación en string del profesor.
        
        Returns:
            str: Representación del profesor incluyendo DNI, nombre, apellido y sueldo.
        """
        return f"Profesor: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Sueldo: {self.sueldo}"
