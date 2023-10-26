/**
 * @file main.cpp
 * @authors Daniel Hurtaodo (A01707774), Gamaliel Marines (A017087467), Carlos Velazco (A01708428)
 * @brief Programa que implementa los algoritmos de Dijkstra y Floyd-Warshall para encontrar las distancias más cortas entre todos los pares de nodos de un grafo.
 * @version 0.1
 * @date 2023-10-22
 * @c g++ -std=c++11 -o main main.cpp
 * @copyright Copyright (c) 2023
 * 
 */

#include <iostream>
#include <vector>
#include <climits>

using namespace std;

/**
 * @brief Imprime una matriz. Si un valor es igual a INT_MAX, se imprime como "INF".
 * @param matrix Matriz a imprimir.
 */

void printMatrix(vector<vector<int>> &matrix) {
    for (const auto &row : matrix) {
        for (int dist : row) {
            if (dist == INT_MAX) {
                cout << "INF ";
            } else {
                cout << dist << " ";
            }
        }
        cout << endl;
    }
}

/**
 * @brief Implementación del algoritmo de Dijkstra.
 * 
 * Encuentra el camino más corto desde un nodo origen 'src' a todos los otros nodos en un grafo.
 * 
 * @param graph Matriz de adyacencia del grafo.
 * @param n Número de nodos en el grafo.
 * @param src Nodo origen.
 * 
 * @return No retorna valor, pero imprime las distancias desde el nodo origen a todos los otros nodos.
 * 
 * @note Complejidad: O(n^2)
 */

void dijkstra(vector<vector<int>> &graph, int n, int src) {
    vector<int> dist(n, INT_MAX);
    vector<bool> visited(n, false);

    dist[src] = 0;

    for (int count = 0; count < n - 1; count++) {
        int u = -1;
        for (int v = 0; v < n; v++) {
            if (!visited[v] && (u == -1 || dist[v] < dist[u])) {
                u = v;
            }
        }

        visited[u] = true;

        for (int v = 0; v < n; v++) {
            if (!visited[v] && graph[u][v] != -1) {
                dist[v] = min(dist[v], dist[u] + graph[u][v]);
            }
        }
    }

    cout << "Dijkstra:" << endl;
    for (int i = 0; i < n; i++) {
        if (i != src) {
            cout << "Distance from node " << src + 1 << " to node " << i + 1 << ": " << dist[i] << endl;
        }
    }
}

/**
 * @brief Implementación del algoritmo de Floyd-Warshall.
 * 
 * Encuentra la distancia más corta entre todos los pares de nodos en un grafo.
 * 
 * @param graph Matriz de adyacencia del grafo.
 * @param n Número de nodos en el grafo.
 * 
 * @return No retorna valor, pero imprime la matriz de distancias entre todos los pares de nodos.
 * 
 * @note Complejidad: O(n^3)
 */

void floydWarshall(vector<vector<int>> &graph, int n) {
    vector<vector<int>> dist(graph);

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][k] != -1 && dist[k][j] != -1) {
                    if (dist[i][j] == -1 || dist[i][j] > dist[i][k] + dist[k][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
    }

    cout << "Floyd:" << endl;
    printMatrix(dist);
}

/**
 * @brief Punto de entrada principal.
 * 
 * Solicita al usuario la matriz de adyacencia del grafo y ejecuta los algoritmos de Dijkstra y Floyd-Warshall.
 * 
 * @return 0 si la ejecución fue exitosa.
 */

int main() {
    int n;
    cout << "Enter the number of nodes: ";
    cin >> n;

    vector<vector<int>> graph(n, vector<int>(n));

    cout << "Enter the adjacency matrix (" << n << "x" << n << "):" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> graph[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        dijkstra(graph, n, i);
    }

    floydWarshall(graph, n);

    return 0;
}
