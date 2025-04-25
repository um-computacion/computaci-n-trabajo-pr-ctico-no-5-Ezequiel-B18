class Persona:
    """Clase base que representa a una persona.
    
    Esta clase modela el comportamiento básico de una persona,
    incluyendo atributos básicos de identificación y la capacidad
    de pensar (registrar ideas).
    
    Attributes:
        nombre (str): Nombre de la persona.
        apellido (str): Apellido de la persona.
        dni (str): Documento Nacional de Identidad.
        pensamientos (int): Contador de pensamientos registrados.
        ultima_idea (str): Último pensamiento registrado por la persona.
    """
    
    def __init__(self, nombre, apellido, dni):
        """Inicializa una nueva instancia de Persona.
        
        Args:
            nombre (str): Nombre de la persona.
            apellido (str): Apellido de la persona.
            dni (str): Documento Nacional de Identidad.
            
        Raises:
            ValueError: Si el DNI está vacío o tiene menos de 8 caracteres.
        """
        if not dni or len(dni) < 8:
            raise ValueError ("El DNI debe tener al menos 8 caracteres.")
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.pensamientos = 0
        self.ultima_idea = "<No penso en nada>"

    def __repr__(self):
        """Devuelve una representación en string de la persona.
        
        Returns:
            str: Representación de la persona incluyendo DNI, nombre, apellido y última idea.
        """
        return f"Persona: DNI: {self.dni}, Nombre: {self.nombre}, Apellido: {self.apellido}, Ultima Idea:{self.ultima_idea}"
    
    def pensar(self, idea):
        """Registra un nuevo pensamiento para la persona.
        
        Este método incrementa el contador de pensamientos y
        actualiza el atributo ultima_idea.
        
        Args:
            idea (str): El pensamiento a registrar.
        """
        self.pensamientos += 1
        self.ultima_idea = idea


