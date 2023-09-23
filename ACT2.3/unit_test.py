import os
from hashing import calcular_hash


def run_all_tests():
    # Directory for the test files
    directory = "ACT2.3"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Test cases
    test_files = {
        "empty.txt": "",
        "exact.txt": "ABCDEFGHIJKLMNOP",
        "large.txt": "ABCDEFGHIJKLMNOPQRSTUVWXYYZabcdefghijklmnopqrstuvwxyyz123456",
        "lines.txt": "ABCD\nEFGH\nIJKL\nMNOP",
        "texto1.txt": "esto es una prueba\ndel algoritmo de\nhash string\nno se que mas\nponer en este archivo",
    }

    for filename, content in test_files.items():
        with open(os.path.join(directory, filename), "w") as file:
            file.write(content)
        print(f"Caso de prueba ({filename}):")
        calcular_hash(os.path.join(directory, filename), len(content))


if __name__ == "__main__":
    run_all_tests()
