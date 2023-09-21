#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <sstream>

using namespace std;

// Función para procesar el archivo y llenar la tabla y el arreglo a
void procesarArchivo(const string& filename, int n, vector<vector<char>>& table, vector<int>& a) {
    ifstream file(filename);
    char c;

    while (file.get(c)) {
        table.push_back(vector<char>(n, ' '));
        table.back()[0] = c;

        for (int i = 1; i < n; ++i) {
            if (file.get(c)) {
                table.back()[i] = c;
            } else {
                table.back()[i] = ' ';
            }
        }

        int column_sum = 0;
        for (int i = 0; i < n; ++i) {
            column_sum += static_cast<int>(table.back()[i]);
            cout<<table.back()[i];
            
        }
        a.push_back(column_sum % 256);
        cout<<a.back()<<endl;
    }

    file.close();
}

// Función para mostrar la tabla
void mostrarTabla(const vector<vector<char>>& table) {
    cout << "Tabla:" << endl;
    for (const vector<char>& row : table) {
        for (char cell : row) {
            cout << cell;
        }
        cout << endl;
    }
}

// Función para mostrar el arreglo a
void mostrarArreglo(const vector<int>& a, int n) {
    cout << "Arreglo a:" << endl;
    for (int i = 0; i < n; ++i) {
        cout << a[i] << " ";
    }
    cout << endl;
}

// Función para generar y mostrar la cadena de salida en formato hexadecimal
void mostrarSalidaHexadecimal(const vector<int>& a, int n) {
    cout << "Cadena de salida en formato hexadecimal:" << endl;
    stringstream hex_output;
    for (int i = 0; i < n; i += 4) {
        int hex_value = 0;
        for (int j = 0; j < 4; ++j) {
            hex_value = (hex_value << 8) | a[i + j];
        }
        hex_output << setw(2) << setfill('0') << hex << hex_value;
    }
    cout << hex_output.str() << endl;
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

    vector<vector<char>> table;
    vector<int> a(n, 0);

    procesarArchivo(filename, n, table, a);
    mostrarTabla(table);
    mostrarArreglo(a, n);
    mostrarSalidaHexadecimal(a, n);

    return 0;
}
