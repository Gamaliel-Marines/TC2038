#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <sstream>

using namespace std;

// Función para procesar el archivo y calcular el hash
string calcularHash(const string& filename, int n) {
    ifstream file(filename);

    if (!file) {
        cerr << "No se pudo abrir el archivo." << endl;
        exit(1);
    }

    vector<int> column_sums(n, 0);

    char c;
    int col = 0;

    while (file.get(c)) {
        column_sums[col] += static_cast<int>(c);
        col = (col + 1) % n;
    }

    file.close();

    stringstream hash_stream;
    for (int i = 0; i < n; ++i) {
        hash_stream << setw(2) << setfill('0') << hex << (column_sums[i] % 256);
    }

    return hash_stream.str();
}

int main() {
    string filename;
    int n;

    cout << "Ingrese el nombre del archivo de texto: ";
    cin >> filename;
    cout << "Ingrese el valor de n (debe ser múltiplo de 4 y estar en el rango [16, 64]): ";
    cin >> n;

    if (n % 4 != 0 || n < 16 || n > 64) {
        cout << "El valor de n no es válido. Debe ser múltiplo de 4 y estar en el rango [16, 64]." << endl;
        return 1;
    }

    string hash = calcularHash(filename, n);

    cout << "Hash calculado: " << hash << endl;

    return 0;
}
