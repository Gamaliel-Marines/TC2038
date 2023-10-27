#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * @brief Función para resolver el problema de la mochila y calcular el beneficio óptimo
 * 
 * @complexity O(N * M)
 * @param N 
 * @param beneficios 
 * @param pesos 
 * @param W 
 * @return int 
 */
int knapsack(int N, vector<int> beneficios, vector<int> pesos, int W) {
    // Crear una matriz dp para almacenar los valores óptimos
    vector<vector<int>> dp(N + 1, vector<int>(W + 1, 0));

    // Llenar la matriz dp utilizando programación dinámica
    for (int i = 1; i <= N; i++) {
        for (int w = 0; w <= W; w++) {
            if (pesos[i - 1] > w) {
                // Si el peso del elemento es mayor que la capacidad, no se puede incluir
                dp[i][w] = dp[i - 1][w]; // Tomar el valor anterior
            } else {
                // Calcular el máximo entre excluir o incluir el elemento
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - pesos[i - 1]] + beneficios[i - 1]);
            }
        }
    }

    // Mostrar la matriz generada
    cout << "Matriz generada:" << endl;
    for (int i = 0; i <= N; i++) {
        for (int w = 0; w <= W; w++) {
            cout << dp[i][w] << "\t";
        }
        cout << endl;
    }

    // El valor en dp[N][W] es el beneficio óptimo
    return dp[N][W];
}

/**
 * @brief Función principal del programa
 * @complexity O(N)
 * 
 * @return int 
 */
int main() {
    int N;
    cout << "Ingrese el número de elementos: ";
    cin >> N;
    vector<int> beneficios(N);
    vector<int> pesos(N);

    cout << "Ingrese los beneficios de cada elemento:" << endl;
    for (int i = 0; i < N; i++) {
        cin >> beneficios[i];
    }

    cout << "Ingrese los pesos de cada elemento:" << endl;
    for (int i = 0; i < N; i++) {
        cin >> pesos[i];
    }

    int W;
    cout << "Ingrese el peso máximo de la mochila: ";
    cin >> W;

    int gananciaOptima = knapsack(N, beneficios, pesos, W);

    cout << "Beneficio óptimo: " << gananciaOptima << endl;

    return 0;
}
