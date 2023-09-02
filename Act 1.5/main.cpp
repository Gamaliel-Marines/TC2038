/**
 * @file main.cpp
 * @author Daniel Hurtado - A01707774
 * @author Carlos Velasco - A01708634
 * @author Gamaliel Marines - 
 * @brief 
 * @version 0.1
 * @date 2023-08-31
 * 
 * @copyright Copyright (c) 2023
 * 
 */

/*

Example input:
    4 -> Number of bills
    5 -> Bill 1
    25 -> Bill 2
    10 -> Bill 3
    50  -> Bill 4
    325 -> Price
    500 -> Amount Payed

Example output:
    Greedy Algorithm
    3 -> 50
    1 -> 25
    0 -> 10
    0 -> 5

    Dynamic Programming
    3 -> 50
    1 -> 25
    0 -> 10
    0 -> 5

*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

/**
 * @brief Function that calculates the change using Dynamic Programming
 * 
 * @param amount 
 * @param coins 
 * @return vector<int> 
 * @complexity O(n^2)
 */

vector<int> coinChangeDP(int amount, vector<int>& coins) {
    vector<int> dp(amount + 1, INT_MAX - 1);
    vector<int> count(coins.size(), 0);
    dp[0] = 0;

    for (int i = 1; i <= amount; ++i) {
        for (int j = 0; j < coins.size(); ++j) {
            if (i >= coins[j]) {
                dp[i] = min(dp[i], dp[i - coins[j]] + 1);
            }
        }
    }

    int remaining = amount;
    while (remaining > 0) {
        for (int j = 0; j < coins.size(); ++j) {
            if (remaining >= coins[j] && dp[remaining] == dp[remaining - coins[j]] + 1) {
                count[j]++;
                remaining -= coins[j];
                break;
            }
        }
    }

    return count;
}

/**
 * @brief Function that calculates the change using Greedy Algorithm
 * 
 * @param amount 
 * @param coins 
 * @return vector<int> 
 * @complexity O(n)
 */

vector<int> coinChangeGreedy(int amount, vector<int>& coins) {
    vector<int> count(coins.size(), 0);
    for (int i = 0; i < coins.size(); ++i) {
        while (amount >= coins[i]) {
            amount -= coins[i];
            count[i]++;
        }
    }
    return count;
}

/**
 * @brief Function that compares to files to see if they are equal
 * 
 * @param file1 
 * @param file2 
 * @return true 
 * @return false 
 * @complexity O(n)
 */
bool compareFiles(const string& fileName1, const string& fileName2) {
    ifstream file1(fileName1);
    ifstream file2(fileName2);
    
    if (!file1.is_open() || !file2.is_open()) {
        cerr << "Error: Couldn't open one of the files for comparison." << endl;
        return false;
    }
    
    string line1, line2;
    while (getline(file1, line1) && getline(file2, line2)) {
        if (line1 != line2) {
            return false;
        }
    }

    return true;
}

/**
 * @brief Main function
 * 
 * @return int 
 * @complexity O(n^2)
 */

int main() {
    int counter = 0;
    for (int fileNum = 1; fileNum <= 4; ++fileNum) {
        ifstream inFile("inputs/input" + to_string(fileNum) + ".txt");
        ofstream outFile("outputs/output" + to_string(fileNum) + ".txt");

        if (!inFile.is_open()) {
            cerr << "Error: No se pudo abrir el archivo de entrada " << fileNum << endl;
            continue;
        }

        if (!outFile.is_open()) {
            cerr << "Error: No se pudo abrir el archivo de salida " << fileNum << endl;
            continue;
        }
        int N, P, Q;
        inFile >> N;

        vector<int> coins(N);
        for (int i = 0; i < N; ++i) {
            inFile >> coins[i];
        }

        inFile >> P >> Q;

        sort(coins.rbegin(), coins.rend());
        int change = Q - P;

        vector<int> dpResult = coinChangeDP(change, coins);
        vector<int> greedyResult = coinChangeGreedy(change, coins);

        outFile << "Greedy Algorithm" << endl;
        for (int i = 0; i < N; ++i) {
            outFile << greedyResult[i] << " -> " << coins[i] << endl;
        }

        outFile << endl << "Dynamic Programming" << endl;
        for (int i = 0; i < N; ++i) {
            outFile << dpResult[i] << " -> " << coins[i] << endl;
        }

        inFile.close();
        outFile.close();

        // Compare the output file with the test case file
        string testFileName = "test_cases/test" + to_string(fileNum) + ".txt";
        if (compareFiles("outputs/output" + to_string(fileNum) + ".txt", testFileName)) {
            counter++;
            cout << "Test case " << fileNum << " passed. (" << counter << "/4) ✅"<< endl;
        } else {
            cout << "Test case " << fileNum << " failed. (" << counter << "/4) ❌"<< endl;
        }
    }

    return 0;
}
