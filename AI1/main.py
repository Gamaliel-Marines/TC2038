# Description: Actividad Integradora 1
# Autores: Daniel Hurtado
#          Carlos Velazco
#          Gamaliel Marines
# Fecha: 29-09-2023


# Importar librerias
import os

# Complejidad: O(n) donde n es el numero de caracteres en el archivo


def read_file(filepath):
    if not os.path.exists(filepath):
        print(f"Error: El archivo {filepath} no existe.")
        return None
    with open(filepath, "r") as file:
        return file.read()


# Complejidad: O(n * m) donde n es el numero de caracteres en el archivo y m es el numero de caracteres en el mcode


def find_all_occurrences(mcode, transmission):
    start = 0
    positions = []
    while True:
        position = transmission.find(mcode, start)
        if position != -1:
            end_position = position + len(mcode) - 1
            positions.append((position, end_position))
            start = position + 1
        else:
            break
    return positions


# Complejidad: O(m * n) donde m es el numero de caracteres en la primera cadena y n es el numero de caracteres en la segunda cadena


def longest_common_substring(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    end, max_length = 0, 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end = i - 1
    if max_length == 0:
        return None, None
    return end - max_length + 1, end


# Complejidad: O(n^2) donde n es el numero de caracteres en la cadena


def longest_palindrome(s):
    # Esta función retorna el inicio y el final del palíndromo más largo en 's'
    max_len = 1
    start = 0
    for i in range(1, len(s)):
        # Buscar palíndromos de longitud par
        low, high = i - 1, i
        while low >= 0 and high < len(s) and s[low] == s[high]:
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1

        # Buscar palíndromos de longitud impar
        low, high = i - 1, i + 1
        while low >= 0 and high < len(s) and s[low] == s[high]:
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1

    return start, start + max_len - 1


def main():
    mcode_dir = 'input/mcode'
    transmission_dir = 'input/transmission'
    
    mcodes = [read_file(os.path.join(mcode_dir, f'mcode0{i}.txt')) for i in range(1, 4)] # Ajustar el rango de acuerdo al numero de mcodes
    transmissions = [read_file(os.path.join(transmission_dir, f'transmission0{i}.txt')) for i in range(1, 3)] # Ajustar el rango de acuerdo al numero de transmisiones
    
    for j, transmission in enumerate(transmissions, start=1):
        print(f"{j}. Transmission{j} {'-'*18}\n")
        for i, mcode in enumerate(mcodes, start=1):
            occurrences = find_all_occurrences(mcode, transmission)
            if occurrences:
                for start_position, end_position in occurrences:
                    print(f"mcode{i}\n(true) Posicion inicial: {start_position} Posicion final: {end_position}\n")
            else:
                print(f"mcode{i}\n(false) Cadena no encontrada en la transmission\n")

        if longest_palindrome(transmission):
                print(f"Longest Palindrome: {longest_palindrome(transmission)}\n")

    lcs_start1, lcs_end1 = longest_common_substring(transmissions[0], transmissions[1])
    if lcs_start1 is None:
        print("no se encontro ningun substring compartido entre ambas transmisiones")
    else:
        print(f"Longest Common Substring: {lcs_start1} {lcs_end1}")


if __name__ == "__main__":
    main()
