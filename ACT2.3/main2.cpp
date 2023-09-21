#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <sstream>

using namespace std;


void mostrarError(const string& mensaje) {
    cerr << "Error: " << mensaje << endl;
}

void mostrarMensaje(const string& mensaje) {
    cout << mensaje << endl;
}

void imprimirContenidoArchivo(const string& filename) {
    ifstream file(filename);

    if (!file) {
        mostrarError("No se pudo abrir el archivo.");
        exit(1);
    }

    string linea;
    mostrarMensaje("Contenido del archivo:");

    while (getline(file, linea)) {
        cout << linea << endl;
    }

    file.close();
}


string calcularHash(const string& filename, int n) {
    ifstream file(filename);

    if (!file) {
        mostrarError("No se pudo abrir el archivo.");
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
        cout << setw(2) << setfill('0') << hex << (column_sums[i] % 256) << endl;
    }

    return hash_stream.str();
}

int main() {
    string filename;
    int n;
    cout<<endl;
    mostrarMensaje("Ingrese el nombre del archivo de texto: ");
    cin >> filename;
    cout<<endl;
    mostrarMensaje("Ingrese el valor de n (debe ser múltiplo de 4 y estar en el rango [16, 64]): ");
    cin >> n;
    cout<<endl;

    if (n % 4 != 0 || n < 16 || n > 64) {
        mostrarError("El valor de n no es válido. Debe ser múltiplo de 4 y estar en el rango [16, 64].");
        return 1;
    }

    string hash = calcularHash(filename, n);
    cout<<endl;

    imprimirContenidoArchivo(filename);
    cout << endl;

    mostrarMensaje("Hash calculado: " + hash);

    

    return 0;
}
