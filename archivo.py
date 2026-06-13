import csv
ARCHIVO = 'paises_prueba.csv'
CAMPOS = ['nombre', 'poblacion', 'superficie', 'continente']

def leer_filas() -> list:
    """
    Lee el archivo csv de países y retorna sus filas como lista de diccionarios.

    Saltea las filas vacias y normaliza los datos: convierte población y superficie a enteros y elimina espacios en el nombre del continente.
    """
    filas = []
    try:
        with open(ARCHIVO, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Saltear fila si todos los campos estan vacios
                if not any(fila.values()):
                    continue
                try:
                    filas.append({
                    'nombre': fila['nombre'],
                    'poblacion': int(fila['poblacion']),
                    'superficie': int(fila['superficie']),
                    'continente': fila['continente'].strip()
                })
                except (ValueError, KeyError, AttributeError):
                    print(f"Fila con formato inválido, se omite: {fila}")

    except FileNotFoundError:
        print(f'El archivo {ARCHIVO} no existe.')
    except Exception as e:
        print(f'Error inesperado: {e}')
    return filas   

def escribir_pais(nombre, poblacion, superficie, continente) -> None:
    """
    Agrega los valores ingresados por el usuario al archivo csv usando csv.writer.
    """
    try:
        with open(ARCHIVO, 'a', encoding='utf-8', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([nombre, poblacion, superficie, continente])
    except Exception as e:
        print(f'Error al escribir en el archivo: {e}')

def reescribir_archivo(paises: list) -> None:
    """
    Reescribe los valores de superficie y población en el archivo csv.
    """
    try:
        with open(ARCHIVO, 'w', encoding='utf-8', newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writeheader()
            for pais in paises:
                escritor.writerow(pais)
    except Exception as e:
        print(f'Error al escribir en el archivo: {e}')