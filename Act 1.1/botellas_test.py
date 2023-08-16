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
    
    def test_volumenContenedor1(self):
        self.assertAlmostEqual(volumenContenedor(2, 10), math.pi * 2 ** 2 * 10)
        
    def test_volumenContenedor2(self):
        self.assertAlmostEqual(volumenContenedor(1, 5), math.pi * 1 ** 2 * 5)
        
    def test_llenarRefresco1(self):
        self.assertAlmostEqual(llenarRefresco(2, 10), (math.pi * 2 ** 2 * 10) / 0.5)
        
    def test_llenarRefresco2(self):
        self.assertAlmostEqual(llenarRefresco(1, 5), (math.pi * 1 ** 2 * 5) / 0.5)

if __name__ == "__main__":
    unittest.main()