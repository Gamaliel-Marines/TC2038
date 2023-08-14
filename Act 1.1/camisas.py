import random

TOTAL_CAMISAS = 30000


def diasProduccion():
    maquina1 = random.randint(200,1000)
    maquina2 = random.randint(200,1000)
    suma = maquina1 + maquina2
    dias = 0
    while TOTAL_CAMISAS < suma:
        dias+=1
    
    print(dias)
    
diasProduccion()