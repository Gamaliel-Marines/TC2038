#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int N = 5;  
const int M = 5;  


/**
 * @brief Checks if a cell is a valid move within the labyrinth. 
 * 
 * @param x 
 * @param y 
 * @param labyrinth 
 * @return true 
 * @return false 
 * @complejidad O(1)
 */
bool isSafe(int x, int y, vector<vector<int>>& labyrinth) {
    return (x >= 0 && x < N && y >= 0 && y < M && labyrinth[x][y] == 1);
}

/**
 * @brief Solves the labyrinth using the backtracking algorithm.
 * 
 * @param labyrinth 
 * @param x 
 * @param y 
 * @return true 
 * @return false 
 * @complexity O(4^(N*M))
 */
bool solveLabyrinthBacktracking(vector<vector<int>>& labyrinth, int x, int y) {
    
    if (x == N - 1 && y == M - 1) {
        return true;
    }

    
    if (isSafe(x, y, labyrinth)) {
    
        labyrinth[x][y] = 2;  

        
        if (solveLabyrinthBacktracking(labyrinth, x + 1, y) ||     
            solveLabyrinthBacktracking(labyrinth, x, y + 1) ||     
            solveLabyrinthBacktracking(labyrinth, x - 1, y) ||     
            solveLabyrinthBacktracking(labyrinth, x, y - 1)) {     
            return true;
        }
    }

    return false;
}

/**
 * @brief Sets unvisited cells to zero in the labyrinth. 
 * 
 * @param labyrinth 
 * @complexity O(N*M)
 */
void updateUnvisitedCells(vector<vector<int>>& labyrinth) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (labyrinth[i][j] == 1) {
                labyrinth[i][j] = 0;  
            }
        }
    }
}

/**
 * @brief Prints the labyrinth.
 * 
 * @param labyrinth 
 * @complexity O(N*M)
 */
void printLabyrinth(const vector<vector<int>>& labyrinth) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cout << labyrinth[i][j] << " ";
        }
        cout << endl;
    }
}
/**
 * @brief Main Function
 * 
 * @return int 
 * @complexity O(4^(N*M)) 
 */
int main() {
    vector<vector<int>> labyrinth = {
        {1, 0, 1, 1, 1},
        {1, 0, 1, 0, 1},
        {1, 1, 1, 1, 1},
        {0, 1, 0, 0, 1},
        {1, 1, 1, 1, 1}
    };

    cout << "Labyrinth:" << endl;
    printLabyrinth(labyrinth);

    cout << "\nSolving using Backtracking:" << endl;
    vector<vector<int>> labyrinthBacktracking = labyrinth;  
    if (solveLabyrinthBacktracking(labyrinthBacktracking, 0, 0)) {
        cout << "Path found:" << endl;
        printLabyrinth(labyrinthBacktracking);
    } else {
        cout << "No path found." << endl;
    }


    cout << "\nBacktracking Solution with Unvisited 1s Changed to 0s:" << endl;
    updateUnvisitedCells(labyrinthBacktracking);
    printLabyrinth(labyrinthBacktracking);



    return 0;
}
