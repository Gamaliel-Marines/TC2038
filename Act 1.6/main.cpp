/**
 * @file main.cpp
 * @authors Daniel Hurtaodo (A01707774), Gamaliel Marines (A017087467), Carlos Velasco
 * @brief Maze solver using backtracking and branch and bound
 * @version 0.1
 * @date 2023-09-10
 * 
 * @copyright Copyright (c) 2023
 * @run g++ main.cpp -o main && ./main
 */


#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

/**
 * @brief Reads a maze from a file and returns a matrix of integers
 * 
 * @param filepath 
 * @return vector< vector<int> > 
 * @complexity O(N*M)
 */
vector< vector<int> > readMaze(const string& filepath) {
    ifstream file(filepath.c_str());
    if (!file) {
        cerr << "No se pudo abrir el archivo: " << filepath << endl;
        exit(EXIT_FAILURE);
    }

    int N, M;
    file >> N >> M;

    vector< vector<int> > maze(N, vector<int>(M));
    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            file >> maze[i][j];
        }
    }
    return maze;
}

/**
 * @brief  Writes a maze solution to a file
 * 
 * @param solution 
 * @param filepath 
 * @complexity O(N*M)
 */
void writeSolution(const vector< vector<int> >& solution, const string& filepath) {
    ofstream file(filepath.c_str());

    for (size_t i = 0; i < solution.size(); ++i){
        for(size_t j = 0; j < solution[i].size(); ++j){
            file << solution[i][j] << " ";
        }
        file << '\n';
    }
}

/**
 * @brief Computes the Manhattan distance between two points.
 * 
 * @param x1 
 * @param y1 
 * @param x2 
 * @param y2 
 * @return int 
 * @complexity O(1)
 */
int manhattanDistance(int x1, int y1, int x2, int y2) {
    return abs(x1 - x2) + abs(y1 - y2);
}

/**
 * @brief Solves the maze using the backtracking algorithm.
 * 
 * @param maze 
 * @param solution 
 * @param x 
 * @param y 
 * @return true 
 * @return false 
 * @complexity O(4^(N*M))
 */
bool solveUsingBacktracking(const vector< vector<int> >& maze, vector< vector<int> >& solution, int x, int y) {
    int M = maze.size();
    int N = maze[0].size();

    if (x == M - 1 && y == N - 1 && maze[x][y] == 1){
        solution[x][y] = 1;
        return true;
    }

    if (x >= 0 && x < M && y >= 0 && y < N && maze[x][y] == 1 && solution[x][y] == 0) {
        solution[x][y] = 1;
        
        if (solveUsingBacktracking(maze, solution, x + 1, y)) return true;
        if (solveUsingBacktracking(maze, solution, x, y + 1)) return true;
        if (solveUsingBacktracking(maze, solution, x - 1, y)) return true;
        if (solveUsingBacktracking(maze, solution, x, y - 1)) return true;

        solution[x][y] = 0;
        return false;
    }
    
    return false;
}

/**
 * @brief Solves the maze using the branch and bound algorithm. 
 * 
 * @param maze 
 * @param solution 
 * @return true 
 * @return false 
 * @complexity O(N * M * log(N * M))
 */
bool solveUsingBranchAndBound(const vector<vector<int> >& maze, vector<vector<int> >& solution) {
    int M = maze.size();
    int N = maze[0].size();

    struct Node {
        int x, y;
        int cost;
    };

    struct Compare {
        int M, N;
        Compare(int M, int N) : M(M), N(N) {}
        bool operator()(const Node& a, const Node& b) const {
            int heuristicA = a.cost + abs(a.x - M + 1) + abs(a.y - N + 1);
            int heuristicB = b.cost + abs(b.x - M + 1) + abs(b.y - N + 1);
            return heuristicA > heuristicB;
        }
    };

    priority_queue<Node, vector<Node>, Compare> pq(Compare(M, N));

    vector<vector<bool> > visited(M, vector<bool>(N, false));
    vector<vector<pair<int, int> > > parent(M, vector<pair<int, int> >(N, make_pair(-1, -1)));

    visited[0][0] = true;

    Node start = {0, 0, 0};
    pq.push(start);

    while (!pq.empty()) {
        Node current = pq.top();
        pq.pop();

        if (current.x == M - 1 && current.y == N - 1) {
            int x = M - 1, y = N - 1;
            while (x != 0 || y != 0) {
                solution[x][y] = 1;
                int tempX = parent[x][y].first;
                int tempY = parent[x][y].second;
                x = tempX;
                y = tempY;
            }
            solution[0][0] = 1;
            return true;
        }

        int directions[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        for (int i = 0; i < 4; ++i) {
            int newX = current.x + directions[i][0];
            int newY = current.y + directions[i][1];

            if (newX >= 0 && newX < M && newY >= 0 && newY < N && maze[newX][newY] == 1 && !visited[newX][newY]) {
                visited[newX][newY] = true;
                parent[newX][newY] = make_pair(current.x, current.y);
                Node next = {newX, newY, current.cost + 1};
                pq.push(next);
            }
        }
    }

    return false;
}
/**
 * @brief Main Function
 * 
 * @return int 
 * @complexity O(N*log(N))
 */
int main() {
    for (int i = 1; i <= 4; ++i) {
        // Leer el laberinto desde un archivo
        vector< vector<int> > maze = readMaze("inputs/input" + to_string(i) + ".txt");
        
        // Obtener las dimensiones del laberinto
        int M = maze.size(), N = maze[0].size();
        
        // Crear matrices para almacenar las soluciones
        vector< vector<int> > solution_backtracking(M, vector<int>(N, 0));
        vector<vector<int> > solution_branch_and_bound(M, vector<int>(N, 0));
        
        // Resolver el laberinto usando backtracking
        solveUsingBacktracking(maze, solution_backtracking, 0, 0);
        solveUsingBranchAndBound(maze, solution_branch_and_bound);
        
        // Escribir las soluciones en archivos
        writeSolution(solution_backtracking, "outputs/backtracking/output" + to_string(i) + ".txt");
        writeSolution(solution_branch_and_bound, "outputs/branch_and_bound/output" + to_string(i) + ".txt");
    }
    
    return 0;
}
