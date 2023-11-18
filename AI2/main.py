import os
import heapq
from itertools import combinations
import math


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
        lines = [line.strip() for line in file.readlines()]

    n = int(lines[0])
    matrix_start = 1
    matrix_end = matrix_start + n
    capacity_matrix_start = matrix_end + 1
    capacity_matrix_end = capacity_matrix_start + n
    coordinates_start = capacity_matrix_end + 1
    coordinates_end = -2

    adjacency_matrix = [
        list(map(int, line.split())) for line in lines[matrix_start:matrix_end]
    ]
    capacity_matrix = [
        list(map(int, line.split()))
        for line in lines[capacity_matrix_start:capacity_matrix_end]
    ]
    coordinates = [
        tuple(map(int, line.replace("(", "").replace(")", "").split(",")))
        for line in lines[coordinates_start:coordinates_end]
    ]
    new_point = tuple(map(int, lines[-1].replace("(", "").replace(")", "").split(",")))

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
    memo = [[None for _ in range(n)] for _ in range(1 << n)]
    path = [[None for _ in range(n)] for _ in range(1 << n)]

    def visit(visited, last):
        if memo[visited][last] is not None:
            return memo[visited][last]

        if visited == (1 << n) - 1:
            return matrix[last][0] if matrix[last][0] > 0 else float('inf')

        min_cost = float('inf')
        for city in range(n):
            if not visited & (1 << city) and matrix[last][city] > 0:
                cost = matrix[last][city] + visit(visited | (1 << city), city)
                if cost < min_cost:
                    min_cost = cost
                    path[visited][last] = city

        memo[visited][last] = min_cost
        return min_cost

    min_cost = visit(1, 0)

    optimal_path = []
    last = 0
    visited = 1
    while True:
        # Convertir el número a letra según la correspondencia dada
        optimal_path.append(chr(last + ord('A')))
        last = path[visited][last]
        if last is None:
            break
        visited |= 1 << last

    optimal_path.append('A')  # Añadir el retorno a la ciudad de origen (1-indexado)
    return min_cost, optimal_path

def max_flow(capacity_matrix, n, start, end):
    """
    Calcula el flujo máximo en una red dada una matriz de capacidad de transmisión de datos.

    Parámetros:
    - capacity_matrix: List[List[int]] - Matriz de capacidad de transmisión de datos.
    - n: int - Número de nodos en la red.
    - start: int - Nodo de inicio.
    - end: int - Nodo final.

    Complejidad:
    - Tiempo: O(E * max_flow), donde E es el número de aristas y max_flow es el flujo máximo.

    Retorna:
    - max_flow: int - Flujo máximo en la red.
    """

    # Inicializa el flujo máximo en 0
    max_flow = 0

    # Mientras haya un camino aumentante
    while True:
        # Encuentra un camino aumentante usando BFS
        path, bottleneck = bfs(capacity_matrix, n, start, end)

        # Si no hay más caminos aumentantes, termina el bucle
        if not path:
            break

        # Actualiza la capacidad residual de las aristas en el camino aumentante
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            capacity_matrix[u][v] -= bottleneck
            capacity_matrix[v][u] += bottleneck

        # Añade el flujo del camino aumentante al flujo máximo total
        max_flow += bottleneck

    return max_flow


def bfs(capacity_matrix, n, start, end):
    """
    Realiza un recorrido BFS para encontrar un camino aumentante en la red.

    Parámetros:
    - capacity_matrix: List[List[int]] - Matriz de capacidad de transmisión de datos.
    - n: int - Número de nodos en la red.
    - start: int - Nodo de inicio.
    - end: int - Nodo final.

    Retorna:
    - path: List[int] - Lista de nodos en el camino aumentante.
    - bottleneck: int - Capacidad mínima de la arista en el camino aumentante.
    """

    # Inicializa el camino y la capacidad mínima en 0
    path = []
    bottleneck = 0

    # Inicializa la lista de nodos visitados
    visited = [False] * n

    # Utiliza una cola para realizar el recorrido BFS
    queue = [start]
    visited[start] = True

    # Inicializa una lista de nodos previos para reconstruir el camino aumentante
    previous_nodes = [-1] * n

    while queue:
        current_node = queue.pop(0)

        # Encuentra las aristas no visitadas con capacidad residual positiva
        for neighbor, capacity in enumerate(capacity_matrix[current_node]):
            if not visited[neighbor] and capacity > 0:
                queue.append(neighbor)
                visited[neighbor] = True
                previous_nodes[neighbor] = current_node

                # Si llegamos al nodo final, reconstruimos el camino aumentante
                if neighbor == end:
                    path = reconstruct_path(previous_nodes, start, end)
                    bottleneck = min(capacity_matrix[u][v] for u, v in zip(path, path[1:]))
                    return path, bottleneck

    return path, bottleneck


def reconstruct_path(previous_nodes, start, end):
    """
    Reconstruye el camino aumentante a partir de los nodos previos.

    Parámetros:
    - previous_nodes: List[int] - Lista de nodos previos en el recorrido BFS.
    - start: int - Nodo de inicio.
    - end: int - Nodo final.

    Retorna:
    - path: List[int] - Lista de nodos en el camino aumentante.
    """

    path = []
    current_node = end

    while current_node != start:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]

    path.insert(0, start)
    return path


def find_closest_central(coordinates, new_point):
    """
    Encuentra la central más cercana geográficamente a una nueva contratación.

    Parámetros:
    - coordinates: List[tuple] - Lista de coordenadas de las centrales.
    - new_point: tuple - Coordenadas de la nueva contratación.

    Retorna:
    - closest_central: int - Índice de la central más cercana.
    """
    closest_central = None
    min_distance = float('inf')

    for i, central_coordinates in enumerate(coordinates):
        distance = calculate_distance(central_coordinates, new_point)
        if distance < min_distance:
            min_distance = distance
            closest_central = i

    return closest_central

def calculate_distance(coord1, coord2):
    """
    Calcula la distancia euclidiana entre dos puntos en el plano.

    Parámetros:
    - coord1: tuple - Coordenadas del primer punto.
    - coord2: tuple - Coordenadas del segundo punto.

    Retorna:
    - distance: float - Distancia entre los dos puntos.
    """
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def main(file_name):
    route = os.path.join("inputs", file_name)
    print(f"Archivo: {file_name}")
    try:
        n, adjacency_matrix, capacity_matrix, coordinates, _ = read_file(route)
        
        print("\nDistancias más cortas entre cada par de ciudades:\n")
        print_shortest_paths(adjacency_matrix, n)

        tsp_cost, tsp_path = tsp(adjacency_matrix, n)
        print(f"\nCosto mínimo del TSP: {tsp_cost}")
        print(f"Ruta del TSP: {tsp_path}")

        max_flow_value = max_flow(capacity_matrix, n, 0, 1)  # Modificar los nodos de inicio y fin según sea necesario
        print(f"\nFlujo máximo: {max_flow_value}")

        # Assuming you want to find the closest central for each input file
        new_point = coordinates[-1]  # Use the last coordinates in the list as the new_point
        closest_central_index = find_closest_central(coordinates[:-1], new_point)  # Exclude the last coordinate
        print(f"\nNueva contratación en coordenadas: {new_point}")
        print(f"La central más cercana es la central {chr(ord('A') + closest_central_index)}\n")
    except FileNotFoundError:
        print(f"No se pudo encontrar o abrir el archivo {route}.")


for i in range(1, 4):
    main(f"input{i}.txt")




