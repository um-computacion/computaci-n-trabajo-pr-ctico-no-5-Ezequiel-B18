import unittest
from src.profesor import Profesor

class TestProfesor(unittest.TestCase):
    def test_crear_profesor(self):
        profesor = Profesor("Juan", "Pérez", "12345678", 50000)
        self.assertEqual(profesor.nombre, "Juan")
        self.assertEqual(profesor.apellido, "Pérez")
        self.assertEqual(profesor.dni, "12345678")
        self.assertEqual(profesor.sueldo, 50000)
    
    def test_repr_profesor(self):
        profesor = Profesor("Juan", "Pérez", "12345678", 50000)
        expected = "Profesor: DNI: 12345678 Nombre: Juan Apellido: Pérez Sueldo: 50000"
        self.assertEqual(str(profesor), expected)

    def test_sueldo_negativo(self):
        with self.assertRaises(ValueError):
            Profesor("Juan", "Pérez", "12345678", -5000)
        
    def test_herencia_metodo_pensar(self):
        profesor = Profesor("Juan", "Pérez", "12345678", 50000)
        profesor.pensar("Una idea de profesor")
        self.assertEqual(profesor.ultima_idea, "Una idea de profesor")
        self.assertEqual(profesor.pensamientos, 1)