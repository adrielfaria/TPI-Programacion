def pais_mayor_poblacion(paises):

    if len(paises) == 0:
        return None

    mayor = paises[0]

    # Recorre la lista buscando el país con más habitantes
    for pais in paises:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais

    return mayor


def pais_menor_poblacion(paises):

    if len(paises) == 0:
        return None

    menor = paises[0]

    for pais in paises:
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

    return menor


def promedio_poblacion(paises):

    if len(paises) == 0:
        return 0

    total = 0
    # Recorre la lista sumando la población de cada país
    for pais in paises:
        total += pais["poblacion"]

    return total / len(paises)


def promedio_superficie(paises):

    if len(paises) == 0:
        return 0

    total = 0
    # Recorre la lista sumando la superficie de cada país
    for pais in paises:
        total += pais["superficie"]

    return total / len(paises)


def cantidad_por_continente(paises):

    continentes = {}

    for pais in paises:

        continente = pais["continente"]
    # Si el continente ya está en el diccionario, incrementa su contador
        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    return continentes


def mostrar_estadisticas(paises):

    if len(paises) == 0:
        print("No hay países cargados.")
        return

    mayor = pais_mayor_poblacion(paises)
    menor = pais_menor_poblacion(paises)

    print("\n===== ESTADÍSTICAS =====")

    print(
        f"País con mayor población: "
        f"{mayor['nombre']} ({mayor['poblacion']})"
    )

    print(
        f"País con menor población: "
        f"{menor['nombre']} ({menor['poblacion']})"
    )

    print(
        f"Promedio de población: "
        f"{promedio_poblacion(paises):.2f}"
    )

    print(
        f"Promedio de superficie: "
        f"{promedio_superficie(paises):.2f}"
    )

    print("\nCantidad de países por continente:")

    continentes = cantidad_por_continente(paises)

    for continente, cantidad in continentes.items():
        print(f"{continente}: {cantidad}")