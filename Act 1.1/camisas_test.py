import random
import unittest

# Código de camisas.py
TOTAL_CAMISAS = 3000

def totalCamisas():
    maquina1 = random.randint(200, 1000)
    maquina2 = random.randint(200, 1000)
    suma = maquina1 + maquina2
    dias = 0
    while TOTAL_CAMISAS > suma:
        maquina1 = random.randint(200, 1000)
        maquina2 = random.randint(200, 1000)
        suma =  suma + maquina1 + maquina2
        dias += 1
    return dias, suma

# Test cases para camisas.py
class TestCamisas(unittest.TestCase):
    
    def test_totalCamisas1(self):
        dias, suma = totalCamisas()
        self.assertTrue(suma >= TOTAL_CAMISAS)
        
    def test_totalCamisas2(self):
        dias, suma = totalCamisas()
        self.assertTrue(suma >= TOTAL_CAMISAS)
        
    def test_totalCamisas3(self):
        dias, suma = totalCamisas()
        self.assertTrue(suma >= TOTAL_CAMISAS)
        
    def test_totalCamisas4(self):
        dias, suma = totalCamisas()
        self.assertTrue(suma >= TOTAL_CAMISAS)

if __name__ == "__main__":
    unittest.main()