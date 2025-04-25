from src.persona import Persona

class Alumno(Persona):
    """Clase que representa a un alumno, hereda de Persona.
    
    Esta clase extiende la clase Persona para modelar a un alumno
    con un número de legajo asociado.
    
    Attributes:
        nombre (str): Heredado de Persona.
        apellido (str): Heredado de Persona.
        dni (str): Heredado de Persona.
        pensamientos (int): Heredado de Persona.
        ultima_idea (str): Heredado de Persona.
        legajo (str): Número de legajo del alumno.
    """
    
    def __init__(self, nombre, apellido, dni, legajo):
        """Inicializa una nueva instancia de Alumno.
        
        Args:
            nombre (str): Nombre del alumno.
            apellido (str): Apellido del alumno.
            dni (str): Documento Nacional de Identidad.
            legajo (str): Número de legajo del alumno.
            
        Raises:
            ValueError: Si el legajo está vacío.
        """
        super().__init__(nombre, apellido, dni)
        if not legajo:
            raise ValueError("El legajo no puede estar vacio.")
        self.legajo = legajo

    def __repr__(self):
        """Devuelve una representación en string del alumno.
        
        Returns:
            str: Representación del alumno incluyendo DNI, nombre, apellido y legajo.
        """
        return f"Alumno: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Legajo: {self.legajo}"