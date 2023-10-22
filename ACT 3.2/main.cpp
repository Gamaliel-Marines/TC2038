#include <iostream>
#include <vector>
#include <climits>

using namespace std;

// Función para imprimir la matriz de distancias
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

// Algoritmo de Dijkstra
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

// Algoritmo de Floyd-Warshall
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
