# Description: Actividad Integradora 1
# Autores: Daniel Hurtado
#          Carlos Velazco
#          Gamaliel Marines
# Fecha: 29-09-2023


# Importar librerias
import os


def read_file(filepath):
    with open(filepath, "r") as file:
        return file.read()


def main():
    mcode_dir = "input/mcode"
    transmission_dir = "input/transmission"

    mcodes = [read_file(os.path.join(mcode_dir, f"mcode0{i}.txt")) for i in range(1, 4)]
    transmissions = [
        read_file(os.path.join(transmission_dir, f"transmission0{i}.txt"))
        for i in range(1, 3)
    ]

    for i, mcode in enumerate(mcodes, start=1):
        for j, transmission in enumerate(transmissions, start=1):
            position = transmission.find(mcode)
            is_contained = position != -1
            print(
                f'Mcode{i} in Transmission{j}: {is_contained} {position if is_contained else ""}'
            )

if __name__ == "__main__":
    main()