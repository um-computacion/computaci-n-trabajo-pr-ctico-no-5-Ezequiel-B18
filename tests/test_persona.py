import unittest
from src.persona import Persona

class TestPersona(unittest.TestCase):
    def test_crear_persona(self):
        persona = Persona("Juan", "Perez", "12345678")
        self.assertEqual(persona.nombre, "Juan")  
        self.assertEqual(persona.apellido, "Perez")  
        self.assertEqual(persona.dni, "12345678")

    def test_repr_persona(self):
        persona = Persona("Juan", "Perez", "12345678")
        expected = "Persona: DNI: 12345678, Nombre: Juan, Apellido: Perez, Ultima Idea:<No penso en nada>"
        self.assertEqual(str(persona), expected)

    def test_pensar_incrementar_contador(self):
        persona = Persona("Juan","Perez" ,"12345678")
        persona.pensar("Hola mundo")
        self.assertEqual(persona.pensamientos, 1)

    def test_pensar_actualiza_ultima_idea(self):
        persona = Persona("Juan","Perez" ,"12345678")
        persona.pensar("Hola mundo")
        self.assertEqual(persona.ultima_idea, "Hola mundo")

