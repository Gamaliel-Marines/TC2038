#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * @brief Calculate the array of substrings within a string
 * 
 * @param s 
 * @return vector<string> 
 */
vector<string> calculateSubstrings(string s){
    vector<string> substrings;
    for (size_t i = 0; i < s.length(); i++) {
        for (size_t j = 1; j <= s.length() - i; j++) {
            string substring = s.substr(i, j);
            substrings.push_back(substring);
        }
    }
    return substrings;
}

/**
 * @brief Prints the array of substrings in the console
 * 
 * @param substr 
 */
void printSubstrings(vector<string> substr){
    cout << "Substrings ordenados alfabéticamente:" << endl;
    for (const string& substring : substr) {
        cout << substring << endl;
    }
}

int main() {
    string input = "mississippi";

    vector<string> substrings = calculateSubstrings(input);

    sort(substrings.begin(), substrings.end());

    printSubstrings(substrings);

    return 0;
}
