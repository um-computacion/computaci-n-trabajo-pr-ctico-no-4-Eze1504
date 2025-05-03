import unittest
from factorial import factorial_iterativo, factorial_recursivo

class TestFactorial(unittest.TestCase):
    
    def test_factorial_iterativo_casos_base(self):
        """Prueba casos base para la implementación iterativa."""
        self.assertEqual(factorial_iterativo(0), 1)
        self.assertEqual(factorial_iterativo(1), 1)
    
    def test_factorial_iterativo_casos_normales(self):
        """Prueba casos normales para la implementación iterativa."""
        self.assertEqual(factorial_iterativo(5), 120)
        self.assertEqual(factorial_iterativo(10), 3628800)
    
    def test_factorial_iterativo_caso_negativo(self):
        """Prueba que la función maneje correctamente números negativos."""
        with self.assertRaises(ValueError):
            factorial_iterativo(-1)
    
    def test_factorial_recursivo_casos_base(self):
        """Prueba casos base para la implementación recursiva."""
        self.assertEqual(factorial_recursivo(0), 1)
        self.assertEqual(factorial_recursivo(1), 1)
    
    def test_factorial_recursivo_casos_normales(self):
        """Prueba casos normales para la implementación recursiva."""
        self.assertEqual(factorial_recursivo(5), 120)
        self.assertEqual(factorial_recursivo(10), 3628800)
    
    def test_factorial_recursivo_caso_negativo(self):
        """Prueba que la función maneje correctamente números negativos."""
        with self.assertRaises(ValueError):
            factorial_recursivo(-1)

if __name__ == '__main__':
    unittest.main()

