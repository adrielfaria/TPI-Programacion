from archivo import leer_filas

def ordenar_por_nombre() -> list:
    """
    Ordena los países alfabéticamente por nombre de la A a la Z.
    """
    paises = leer_filas()
    nombres_ordenados = sorted(paises, key=lambda pais: pais['nombre'])
    return nombres_ordenados


def ordenar_por_poblacion() -> list:
    """
    Ordena los países por población de menor a mayor.
    """
    paises = leer_filas()
    poblacion_ordenada = sorted(paises, key=lambda pais: pais['poblacion'])
    return poblacion_ordenada

# Ordena los paises en base a su superficie de menor a mayor
def ordenar_por_superficie_asc() -> list:
    """
    Ordena los países por superficie de menor a mayor.
    """
    paises = leer_filas()
    superficie_ascendente = sorted(paises, key=lambda pais: pais['superficie'])
    return superficie_ascendente   

# Ordena los paises en base a su superficie de mayor a menor
def ordenar_por_superficie_desc() -> list:
    """
    Ordena los países por superficie de mayor a menor.
    """
    paises = leer_filas()
    # reverse=True invierte el orden para obtener el resultado descendente
    superficie_descendente = sorted(paises, key=lambda pais: pais['superficie'], reverse=True)
    return superficie_descendente 

# Funcion la cual contendra el menu y resto de funciones de ordenar pais
def ordenar_paises() -> None:
    """
    Muestra un menú interactivo para ordenar y listar los países según distintos criterios.
    """
    # diccionario: asocia cada opción con su función correspondiente
    opciones = {
        '1': ordenar_por_nombre,
        '2': ordenar_por_poblacion,
        '3': ordenar_por_superficie_asc,
        '4': ordenar_por_superficie_desc,
    }

    while True:
        print('\n1. Ordenar por nombre.')
        print('2. Ordenar por población ascendente.')
        print('3. Ordenar por superficie ascendente')
        print('4. Ordenar por superficie descendente')
        print('5. Atrás')
        opcion = input('Escoge una opción: ')

        if opcion == '5':
            break
        funcion = opciones.get(opcion)

        if funcion:
            print('')
            datos = funcion()
            for dato in datos:
                print(f'Pais: {dato["nombre"]} | Poblacion: {dato["poblacion"]} habitantes | Superficie: {dato["superficie"]} km2 | Continente: {dato["continente"]}')
        else:
            print('Opcion Inválida')
