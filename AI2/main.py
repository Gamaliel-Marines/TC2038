import os
import heapq
from itertools import combinations


def read_file(file_name):
    """
    Lee un archivo de texto que contiene matrices de adyacencia, capacidad y coordenadas de nodos.

    Parámetros:
    - file_name: str - Ruta al archivo que será leído.

    Retorna:
    - n: int - Número de nodos del grafo.
    - adjacency_matrix: List[List[int]] - Matriz de adyacencia.
    - capacity_matrix: List[List[int]] - Matriz de capacidad de transmisión de datos.
    - coordinates: List[tuple] - Lista de coordenadas de los nodos.
    """
    with open(file_name, "r") as file:
        lines = file.readlines()

    n = int(lines[0].strip())
    adjacency_matrix = [
        list(map(int, line.strip().split())) for line in lines[1 : n + 1]
    ]
    capacity_matrix = [
        list(map(int, line.strip().split())) for line in lines[n + 1 : 2 * n + 1]
    ]
    coordinates = [
        tuple(map(int, line.strip().split(","))) for line in lines[2 * n + 1 : -1]
    ]
    new_point = tuple(map(int, lines[-1].strip().split(",")))

    return n, adjacency_matrix, capacity_matrix, coordinates, new_point


def dijkstra(matrix, n, start):
    """
    Calcula las distancias más cortas desde un nodo de inicio en una matriz ponderada.

    Parámetros:
    - matrix: List[List[int]] - Matriz de adyacencia que representa el grafo.
    - n: int - Número de nodos en el grafo.
    - start: int - Nodo de inicio para calcular las distancias.

    Complejidad:
    - Tiempo: O(n log n)

    Retorna:
    - distances: List[int] - Lista de distancias más cortas desde el nodo de inicio.
    - previous_nodes: List[int] - Lista de nodos previos en la ruta más corta.
    """

    # Inicializa la lista de distancias con infinito para todos los nodos excepto el nodo de inicio
    distances = [float("inf")] * n
    distances[start] = 0

    # Inicializa una lista de nodos visitados
    visited = [False] * n

    # Inicializa una lista de nodos previos para reconstruir la ruta más corta
    previous_nodes = [-1] * n

    # Utiliza una cola de prioridad (heap) para seleccionar el nodo con la distancia más corta
    priority_queue = [(0, start)]

    while priority_queue:
        # Extrae el nodo con la distancia más corta
        current_distance, current_node = heapq.heappop(priority_queue)

        # Marca el nodo como visitado
        visited[current_node] = True

        # Actualiza las distancias a los nodos adyacentes si se encuentra una distancia más corta
        for neighbor, weight in enumerate(matrix[current_node]):
            if not visited[neighbor] and weight > 0:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes


def print_shortest_paths(matrix, cities):
    """
    Imprime la forma más óptima de conectar cada ciudad desde cada ciudad a todas las demás ciudades.

    Complejidad:
    - Tiempo O(cities^2 * n log n)

    Parámetros:
    - matrix: List[List[int]] - Matriz de adyacencia que representa el grafo.
    - cities: int - Número de ciudades en el grafo.
    """
    # Inicializar el nombre de la primera ciudad
    first_city = "A"

    # Tenemos que iniciar desde cada ciudad disponible para buscar la ruta más corta
    for start_city in range(cities):
        # Imprime cuál es la ciudad que se está tomando como referencia
        print(
            f"La forma más óptima de conectar cada ciudad desde la ciudad {chr(ord(first_city) + start_city)}:"
        )
        # Recorrer cada ciudad destino
        for end_city in range(cities):
            # La ciudad destino no puede ser la ciudad origen
            if start_city != end_city:
                # Utilizar el algoritmo de Dijkstra para obtener la ruta más corta
                distances, previous_nodes = dijkstra(matrix, cities, start_city)
                # Lista para ir guardando cuál es la ruta más óptima
                path = []
                # Guardar en una variable el destino
                current_node = end_city
                # Mientras la ciudad actual no sea la ciudad origen
                while current_node != start_city:
                    # Agregar la ciudad actual a la ruta y pasar a la siguiente ciudad
                    path.insert(0, chr(ord(first_city) + current_node))
                    current_node = previous_nodes[current_node]
                # Insertar la ciudad origen al inicio
                path.insert(0, chr(ord(first_city) + start_city))
                # Hacemos string la lista
                path_str = " -> ".join(path)
                # Ciudad Origen -> Ciudad Destino: Ruta (Distancia km)
                print(
                    f"{chr(ord(first_city) + start_city)} -> {chr(ord(first_city) + end_city)}: {path_str} ({distances[end_city]} km)"
                )


def tsp(matrix, n):
    """
    Resuelve el problema del agente viajero utilizando programación dinámica.

    Parámetros:
    - matrix: List[List[int]] - Matriz de adyacencia que representa el grafo.
    - n: int - Número de nodos en el grafo.

    Retorna:
    - min_cost: int - Costo mínimo para visitar todas las ciudades y regresar a la ciudad de origen.
    - path: List[int] - Secuencia de nodos representando la ruta óptima.
    """
    # Crear una tabla de memorización para almacenar los costos mínimos de visitar cada conjunto de nodos
    memo = [[None] * n for _ in range(1 << n)]
    # Crear una tabla para rastrear el camino óptimo
    path = [[None] * n for _ in range(1 << n)]

    # Función para visitar nodos. "visited" es un bitmask que representa los nodos visitados
    def visit(visited, last):
        # Si ya visitamos este conjunto de nodos y terminamos en 'last', devolver el costo guardado
        if memo[visited][last] is not None:
            return memo[visited][last]

        # Si todos los nodos han sido visitados, devolver la distancia al nodo de inicio (0)
        if visited == (1 << n) - 1:
            return matrix[last][0] if matrix[last][0] > 0 else float("inf")

        # Establecer un costo inicial alto
        min_cost = float("inf")
        # Intentar visitar cada nodo
        for i in range(n):
            # Si el nodo 'i' no ha sido visitado y hay un camino desde 'last' a 'i'
            if not visited & (1 << i) and matrix[last][i] > 0:
                # Calcular el costo de visitar 'i' después de 'last'
                cost = matrix[last][i] + visit(visited | (1 << i), i)
                # Actualizar el costo mínimo y el camino
                if cost < min_cost:
                    min_cost = cost
                    path[visited][last] = i

        # Guardar el costo mínimo en la tabla de memorización
        memo[visited][last] = min_cost
        return min_cost

    # Iniciar la visita desde el nodo 0 con solo el nodo 0 visitado
    min_cost = visit(1, 0)

    # Reconstruir el camino óptimo
    optimal_path = []
    last = 0
    visited = 1
    while True:
        optimal_path.append(last)
        next_node = path[visited][last]
        if next_node is None:
            break
        visited |= 1 << next_node
        last = next_node

    return min_cost, optimal_path


def main(file_name):
    # Guardar en una variable la ruta del archivo
    route = os.path.join("inputs", file_name)
    print(f"Archivo: {file_name}")
    try:
        cities, matrix = read_file(route)
        print_shortest_paths(matrix, cities)
        tsp_cost, tsp_path = tsp(matrix, cities)
        print(f"Costo mínimo del TSP: {tsp_cost}")
        print(f"Ruta del TSP: {tsp_path}")

    except FileNotFoundError:
        print(f"No se pudo encontrar o abrir el archivo {route}.")


for i in range(1, 2):
    main(f"input{i}.txt")
