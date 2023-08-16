# Featured by : 
#| Gamaliel Marines |
#| Daniel Hurtado   |
#| Carlos Velasco   |
# =============================================
# _____________________________________________
# 
# =============================================
# Para poder resolver este problema, se debe
# de calcular el volumen del contenedor y
# dividirlo entre la cantidad de litros que
# contiene una botella de refresco.
#
# Para calcular el volumen de un contenedor
# cilindrico se utiliza la siguiente formula:
# V = pi * r^2 * h
# Donde:
# V = Volumen
# pi = 3.1416
# r = Radio de la base
# h = Altura del contenedor
#
# Para calcular la cantidad de refrescos que
# se pueden llenar con el volumen del contenedor
# se utiliza la siguiente formula:
# Cantidad de refrescos = Volumen / Litros
# Donde:
# Volumen = Volumen del contenedor
# Litros = Cantidad de litros que contiene una
#          botella de refresco
#
# Para poder realizar los calculos se utilizo
# la libreria math, la cual contiene la
# constante pi.
#
# Para poder ejecutar el programa se debe
# de ejecutar el siguiente comando:
# python3 refresco.py
# =============================================
# _____________________________________________

import math

LITROS = 0.5

# Funcion que calcula el volumen de un contenedor
# cilindrico
def volumenContenedor(radioBase, altura):
    # V = pi * r^2 * h
    return math.pi * radioBase ** 2 * altura

# Funcion que calcula la cantidad de refrescos
# que se pueden llenar con el volumen del
# contenedor
def llenarRefresco(radioBase, altura):
    # se manda llamar la funcion volumenContenedor
    # para obtener el volumen del contenedor
    volumen = volumenContenedor(radioBase, altura)
    # Cantidad de refrescos = Volumen / Litros
    return volumen / LITROS

# Funcion principal
if __name__ == "__main__":
    # Se piden los datos al usuario
    radioBase = float(input("Radio del conetendor: "))
    altura = float(input("Altura del contenedor: "))
    # Se imprimen los resultados
    print("Volumen del contenedor: ", volumenContenedor(radioBase, altura))
    print("Cantidad de refrescos: ", llenarRefresco(radioBase, altura))
