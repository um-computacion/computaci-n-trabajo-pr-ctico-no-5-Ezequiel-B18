from src.persona import Persona
from src.profesor import Profesor
from src.alumno import Alumno

def main():
    """Función principal que demuestra el uso de las clases Persona, Profesor y Alumno.
    
    Esta función crea instancias de cada clase, muestra cómo usar el método pensar
    y presenta la representación en string de cada objeto.
    """
    print("Creando persona...")
    persona = Persona("Pepe", "Carlos", "12345678")
    persona.pensar("No esta pensando en nada")
    print(persona)
    print()

    print("Creando profesor...")
    profesor = Profesor("Juan", "Garcia", "23456789", 60000)
    profesor.pensar("¿Que tan dificil hago el examen?")
    print(profesor)
    print()

    print("Creando alumno...")
    alumno = Alumno("Ezequiel", "Blajevitch", "46059811", "64053")
    alumno.pensar("Quiero aprobar computacion")
    print(alumno)

if __name__ == '__main__':
    main()

