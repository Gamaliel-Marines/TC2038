"""
Archivo: hashing.py
Descripción: Implementa un algoritmo de hashing basado en una tabla y la suma de valores ASCII.
Autores:
    - Daniel Hurtaodo (A01707774), 
    - Gamaliel Marines (A017087467), 
    - Carlos Velasco (A01708428),

Instrucciones de Uso:
    1. Ejecutar el archivo unit_test.py para generar los archivos de prueba.
    2. Proporcionar el nombre del archivo y el valor de n como se solicita.
    3. El programa calculará y mostrará el valor hash correspondiente.

Para probar la robustez y precisión del programa, se recomienda correr el archivo 'unit_test.py'.

"""

import os

def mostrar_mensaje(mensaje):
    """ 
    Imprime un mensaje proporcionado.
    
    Parámetros:
    - mensaje (str): El mensaje a imprimir.
    
    Complejidad:
    O(1)
    """
    print(mensaje)


def calcular_hash(filename, n):
    """
    Calcula y muestra el hash de un archivo de texto basado en una tabla y la suma de valores ASCII.
    
    Parámetros:
    - filename (str): El nombre del archivo a procesar.
    - n (int): El número de columnas de la tabla.
    
    Retorna:
    str: La cadena hash generada.
    
    Complejidad:
    O(n*m), donde n es el número de columnas y m es el número de filas de la tabla generada.
    """
    
    # Leer el contenido del archivo
    with open(filename, 'r') as file:
        content = file.read()

    # Si n es 0, regresar un hash estándar
    if n == 0:
        print("Hash: 0000 (Para n = 0)")
        return "0000"
        
    # Crear la tabla
    table = [list(content[i:i+n]) for i in range(0, len(content), n)]
    # Rellenar la última fila si es necesario
    while len(table[-1]) < n:
        table[-1].append(chr(n))

    # Imprimir la tabla
    print("Tabla Generada:")
    for row in table:
        print("".join(row))

    # Calcular las sumas de las columnas
    column_sums = [sum([ord(row[i]) for row in table]) % 256 for i in range(n)]
    
    # Imprimir el arreglo 'a'
    print("Arreglo a:")
    print(" ".join([f"{x:02X}" for x in column_sums]))

    # Generar el hash
    hash_value = "".join([f"{column_sums[i]:02X}" for i in range(n//4)])
    print(f"Hash: {hash_value}\n")
    return hash_value


if __name__ == "__main__":
    filename = input("Por favor ingrese el nombre del archivo: ")
    n = int(input("Por favor ingrese el valor de n (múltiplo de 4 y entre [16, 64]): "))
    calcular_hash(filename, n)
