import unittest
from flatten import flatten

class TestFlatten(unittest.TestCase):
    
    def test_lista_simple(self):
        """Prueba para una lista sin elementos anidados."""
        lista = [1, 2, 3, 4]
        resultado_esperado = [1, 2, 3, 4]
        self.assertEqual(flatten(lista), resultado_esperado)
    
    def test_lista_con_listas_anidadas(self):
        """Prueba para una lista con listas anidadas."""
        lista = [1, [2, 3], [4, [5, 6]]]
        resultado_esperado = [1, 2, 3, 4, 5, 6]
        self.assertEqual(flatten(lista), resultado_esperado)
    
    def test_lista_con_diferentes_estructuras(self):
        """Prueba para una lista con diferentes estructuras anidadas."""
        lista = [1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]
        resultado_esperado = [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8]
        # Convertir todos los elementos a string antes de ordenar
        result_flatten = [str(x) for x in flatten(lista)]
        expected_result = [str(x) for x in resultado_esperado]
        self.assertEqual(sorted(result_flatten), sorted(expected_result))
        
    def test_lista_vacia(self):
        """Prueba para una lista vacía."""
        self.assertEqual(flatten([]), [])
    
    def test_lista_con_valores_nulos(self):
        """Prueba para una lista con valores nulos."""
        lista = [1, None, [2, None]]
        resultado_esperado = [1, None, 2, None]
        self.assertEqual(flatten(lista), resultado_esperado)
         
if __name__ == '__main__':
    unittest.main()
