import os
import heapq


def read_file(file_name):
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
    with open(file_name, "r") as file:
        n = int(file.readline().strip())
        matriz = [list(map(int, line.strip().split())) for line in file]
    return n, matriz

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
    distances = [float('inf')] * n
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
    first_city = 'A'
    
    # Tenemos que iniciar desde cada ciudad disponible para buscar la ruta más corta
    for start_city in range(cities):
        # Imprime cuál es la ciudad que se está tomando como referencia
        print(f"La forma más óptima de conectar cada ciudad desde la ciudad {chr(ord(first_city) + start_city)}:")
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
                print(f"{chr(ord(first_city) + start_city)} -> {chr(ord(first_city) + end_city)}: {path_str} ({distances[end_city]} km)")

def main(file_name):
    # Guardar en una variable la ruta del archivo
    route = os.path.join("inputs", file_name)
    print(f"Archivo: {file_name}")
    try:
        # Leer el archivo y guardar el número de ciudades y la matriz en dos variables
        cities, matriz = read_file(route)
        # Imprimir la ruta más corta para cada 
        print_shortest_paths(matriz, cities)
    except FileNotFoundError:
        print(f"No se pudo encontrar o abrir el archivo {route}.")

for i in range(1,5):
    main(f"input{i}.txt")