import random

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
        print("La cantidad de camisas producidas en el día", dias, "fueron:", suma)

    print("La cantidad de días que se tardaron en producir las", TOTAL_CAMISAS, "camisas fueron:", dias)

totalCamisas()

    
if __name__ == "__main__":
    totalCamisas()