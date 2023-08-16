
import math
import unittest

# Código de botellas.py
LITROS = 0.5

def volumenContenedor(radioBase, altura):
    return math.pi * radioBase ** 2 * altura

def llenarRefresco(radioBase, altura):
    volumen = volumenContenedor(radioBase, altura)
    return volumen / LITROS

# Test cases para botellas.py
class TestBotellas(unittest.TestCase):
    
    def test_volumenContenedor(self):
        self.assertAlmostEqual(volumenContenedor(2, 10), math.pi * 2 ** 2 * 10)
        
    def test_llenarRefresco(self):
        self.assertAlmostEqual(llenarRefresco(2, 10), (math.pi * 2 ** 2 * 10) / 0.5)

# Ejecutamos los tests
if __name__ == "__main__":
    unittest.main()
