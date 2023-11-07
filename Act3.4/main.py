import os


def leer_archivo(nombre_del_archivo):
    """
    Lee un archivo de texto que representa una matriz de adyacencia de un grafo y lo convierte en una lista de listas.

    Parámetros:
    - nombre_del_archivo: str - Ruta al archivo que será leído.

    Complejidad:
    - Tiempo: O(n^2) - Se lee cada elemento de la matriz.

    Retorna:
    - n: int - Número de nodos del grafo.
    - matriz: List[List[int]] - Matriz de adyacencia que representa el grafo.
    """
    with open(nombre_del_archivo, "r") as file:
        n = int(file.readline().strip())
        matriz = [list(map(int, line.strip().split())) for line in file]
    return n, matriz


def ordenar_nodos_por_aristas(matriz):
    """
    Ordena los nodos de un grafo basado en el número de aristas de cada nodo.

    Parámetros:
    - matriz: List[List[int]] - Matriz de adyacencia del grafo.

    Complejidad:
    - Tiempo: O(n^2) - Se recorre cada elemento de la matriz.

    Retorna:
    - nodos_ordenados: List[Tuple[int, int]] - Lista de nodos ordenados por su grado en orden descendente.
    """

    # Contar el número de aristas para cada nodo y mantener su índice original
    aristas_por_nodo = [(i, sum(fila)) for i, fila in enumerate(matriz)]
    # Ordenar primero por el número de aristas (de mayor a menor) y luego por el índice original en caso de empate
    nodos_ordenados = sorted(aristas_por_nodo, key=lambda x: (-x[1], x[0]))
    return nodos_ordenados  # Lista de tuplas (nodo, número de aristas)


def colorear_grafo(matriz):
    """
    Colorea un grafo de manera que dos nodos adyacentes no tengan el mismo color.

    Parámetros:
    - matriz: List[List[int]] - Matriz de adyacencia del grafo.

    Complejidad:
    - Tiempo: O(n^2) - Se recorre cada elemento de la matriz.

    Retorna:
    - colores: List[int] - Lista de colores asignados a cada nodo.
    """

    n = len(matriz)
    nodos_ordenados = ordenar_nodos_por_aristas(matriz)
    colores = [-1] * n

    # Colorear cada nodo
    for nodo_info in nodos_ordenados:
        nodo = nodo_info[0]
        colores_prohibidos = set()

        # Determinar los colores que no se pueden usar para este nodo (colores de nodos adyacentes)
        for adyacente in range(n):
            if matriz[nodo][adyacente] == 1 and colores[adyacente] != -1:
                colores_prohibidos.add(colores[adyacente])

        # Asignar el color más bajo posible que no esté prohibido
        color_actual = 0
        while color_actual in colores_prohibidos:
            color_actual += 1
        colores[nodo] = color_actual

    return colores


def imprimir_colores(colores):
    """
    Imprime los colores asignados a cada nodo del grafo.

    Parámetros:
    - colores: List[int] - Lista de colores asignados a cada nodo.

    Complejidad:
    - Tiempo: O(n) - Se recorre cada elemento de la lista.
    """

    for indice, color in enumerate(colores):
        print(f"Vértice: {indice}, Color asignado: {color}")


def main(nombre_del_archivo):
    """
    Función principal que ejecuta el proceso de lectura, coloración y muestra de resultados del grafo.

    Parámetros:
    - nombre_del_archivo: str - Nombre del archivo de entrada.
    """

    # Construir la ruta completa al archivo dentro de la carpeta "inputs"
    ruta_completa = os.path.join("inputs", nombre_del_archivo)

    try:
        n, matriz = leer_archivo(ruta_completa)
        colores = colorear_grafo(matriz)

        if n == 0:
            print(f"Archivo {nombre_del_archivo}: El grafo está vacío.")
            return

        # Verificación después de colorear para ver si es posible o no
        if any(color == -1 for color in colores):
            print(
                f"Archivo {nombre_del_archivo}: No es posible asignar colores a los nodos."
            )
        else:
            print(f"Archivo {nombre_del_archivo}: Colores asignados a los nodos:")
            imprimir_colores(colores)

    except FileNotFoundError:
        print(f"No se pudo encontrar o abrir el archivo {ruta_completa}.")


archivos = [
    "input1.txt",
    "input2.txt",
    "input3.txt",
    "input4.txt",
    "input5.txt",
    "input6.txt",
    "input7.txt",
]

for archivo in archivos:
    main(archivo)
