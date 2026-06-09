# filtros.py - Funciones para filtrar países según distintos criterios
from validaciones import pedir_texto, pedir_numero
from archivo import leer_filas

def filtrar_por_continente() -> None:
    """
    Pide al usuario ingresar el nombre del continente por el que desea filtrar y devuelve información de los paises que pertenecen a dicho continente.
    """
    continente = pedir_texto('Ingrese el nombre del continente por el que desea filtrar: ')
    paises = leer_filas()
    resultados = []
    for pais in paises:
        # Comparación sin distinguir mayúsculas/minúsculas
        if pais['continente'].lower() == continente.lower():
            resultados.append(pais)
    if not resultados:
        print('No se han encontrado países en ese continente.')
        return
    for pais in resultados:
        print(f'Pais: {pais["nombre"]}, Poblacóon: {pais["poblacion"]}, Superficie: {pais["superficie"]}')


def filtrar_por_poblacion() -> None:
    """
    Pide al usuario ingresar una población mínima y una máxima y devuelve los países que se encuentran dentro de ese rango.
    """
    minima = int(pedir_numero('Población mínima: '))
    maxima = int(pedir_numero('Población máxima: '))
    paises = leer_filas()
    resultados = []
    for pais in paises:
        if minima <= pais['poblacion'] <= maxima:
            resultados.append(pais)
    if not resultados:
        print('No se han encontrado países en ese rango de población.')
        return
    for pais in resultados:
        print(f'Pais: {pais["nombre"]}, Población: {pais["poblacion"]}, Superficie: {pais["superficie"]} Continente: {pais["continente"]}')


def filtrar_por_superficie() -> None:
    """
    Pide al usuario ingresar una superficie mínima y una máxima y devuelve los países que se encuentran dentro de ese rango.
    """
    minima = int(pedir_numero('Superficie mínima: '))
    maxima = int(pedir_numero('Superficie máxima: '))
    paises = leer_filas()
    resultados = []
    for pais in paises:
        if minima <= pais['superficie'] <= maxima:
            resultados.append(pais)
    if not resultados:
        print('No se han encontrado países en ese rango de superficie.')
        return
    for pais in resultados:
        print(f'Pais: {pais["nombre"]}, Población: {pais["poblacion"]}, Superficie: {pais["superficie"]} Continente: {pais["continente"]}')


def filtrar_paises_por() -> None:
    """
    Menu principal que contendra el resto de funciones de filtrar países.
    """
    # Mapeo de opción para evitar if/elif encadenados
    opciones = {
        '1': filtrar_por_continente,
        '2': filtrar_por_poblacion,
        '3': filtrar_por_superficie
    }

    while True:
        print('\n1. Filtrar paises por continente.')
        print('2. Filtrar paises por rango de poblacion.')
        print('3. Filtrar paises por rango de superficie.')
        print('4. Atras')
        opcion = input('Escoge una opcion: ')

        if opcion == '4':
            break
        funcion = opciones.get(opcion)

        if funcion:
            funcion()
        else:
            print('Opcion Invalida')

filtrar_paises_por()

