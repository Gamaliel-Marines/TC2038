# Featured by : 
#| Gamaliel Marines |
#| Daniel Hurtado   |
#| Carlos Velasco   |
# =============================================
# _____________________________________________
# 
# =============================================
#| Una fábrica de camisas tiene dos cadenas de producción para hacer camisas
#| ambas maquinas producen un numero diferente de camisas por día. 
#| Por cuesiones de estudio hemos decidido que la cantidad de camisas producidas
#| por cada maquina sea aleatoria, entre 200 y 1000 camisas por día.
#
#| La fábrica tiene como meta producir 3000 camisas para un pedido.
#| Se desea saber en cuantos días se logrará la meta de producir las 3000 camisas.
#| 
#| Para poder solucionar este problema se debe crear una función que suma la pruduccion de ambas maquina,
#| compare la suma con la meta de 3000 camisas y si no se ha logrado la meta, se debe volver a generar
#| la producción de ambas maquinas y volver a comparar la suma con la meta. Una vez cumplida la meta
#| se debe imprimir la cantidad de camisas producidas por día y la cantidad 
#| de días que se tardó en producir las camisas.



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

    
if __name__ == "__main__":
    totalCamisas()