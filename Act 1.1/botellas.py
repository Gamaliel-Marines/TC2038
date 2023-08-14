import math

LITROS = 0.5

def volumenContenedor(radioBase, altura):
    return math.pi * radioBase ** 2 * altura

def llenarRefresco(radioBase, altura):
    volumen = volumenContenedor(radioBase, altura)
    return volumen / LITROS

if __name__ == "__main__":
    radioBase = float(input("Radio del conetendor: "))
    altura = float(input("Altura del contenedor: "))
    print("Volumen del contenedor: ", volumenContenedor(radioBase, altura))
    print("Cantidad de refrescos: ", llenarRefresco(radioBase, altura))
