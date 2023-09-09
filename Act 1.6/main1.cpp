#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int N = 5;  
const int M = 5;  


bool isSafe(int x, int y, vector<vector<int>>& labyrinth) {
    return (x >= 0 && x < N && y >= 0 && y < M && labyrinth[x][y] == 1);
}

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

void updateUnvisitedCells(vector<vector<int>>& labyrinth) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (labyrinth[i][j] == 1) {
                labyrinth[i][j] = 0;  
            }
        }
    }
}


void printLabyrinth(const vector<vector<int>>& labyrinth) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cout << labyrinth[i][j] << " ";
        }
        cout << endl;
    }
}

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
