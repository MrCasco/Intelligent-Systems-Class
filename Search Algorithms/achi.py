from copy import deepcopy

VACIO, X, O = " ", "X", "O"
MAX, MIN = "max", "min"
GANA_X, GANA_O, EMPATE = 1, -1, 0
INFINITO = 1000

adyacencias = {
    (0,0): [(0,1), (1,0), (1,1)],
    (0,1): [(0,0), (0,2), (1,1)],
    (0,2): [(0,1), (1,2), (1,1)],
    (1,0): [(0,0), (2,0), (1,1)],
    (1,1): [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2)],
    (1,2): [(0,2), (2,2), (1,1)],
    (2,0): [(1,0), (2,1), (1,1)],
    (2,1): [(2,0), (2,2), (1,1)],
    (2,2): [(1,2), (2,1), (1,1)]
}

def imprimirTablero(tablero):
    print("*******")
    for i in tablero:
        print("|", end="")
        for j in i:
            print(j, end="|")
        print("\n*******")

def esTerminal(tablero):
    """
    Revisar si ha ganado algún jugador o si hay empate.
    Si el tablero no es terminal, regresa None
    """
    tiros = [X, O]
    resultados = [GANA_X, GANA_O]

    for tiro, resultado in zip(tiros, resultados):
        for i in range(3):
            # Analizar líneas horizontales
            if tablero[i][0] == tablero[i][1] == tablero[i][2] == tiro:
                return resultado
            # Analizar líneas verticales
            if tablero[0][i] == tablero[1][i] == tablero[2][i] == tiro:
                return resultado
        # Analizar diagonales
        if tablero[0][0] == tablero[1][1] == tablero[2][2] == tiro:
            return resultado
        if tablero[2][0] == tablero[1][1] == tablero[0][2] == tiro:
            return resultado
    # Verificar si hay alguna casilla vacía
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == VACIO:
                return None
    # Si no hay casillas vacías, es un empate
    return EMPATE

def obtenerCasillaVacia(tablero):
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == VACIO:
                return (i,j)
    return None

# def obtenerAdyacencias(tablero, casilla, tiro):
#     for i, j in adyacencias[casilla]:
#         if tablero[i][j] == tiro:
#             yield (i,j)

def obtenerAdyacencias(tablero, casilla, tiro):
    return [(i, j) for i, j in adyacencias[casilla] if tablero[i][j] == tiro]

def realizarMovimiento(tablero, casilla1, casilla2):
    tablero[casilla1[0]][casilla1[1]], tablero[casilla2[0]][casilla2[1]] = \
        tablero[casilla2[0]][casilla2[1]], tablero[casilla1[0]][casilla1[1]]

def minimax(tablero, profundidad, minMax):
    if profundidad < 8:
        return minimaxGato(tablero, profundidad, minMax)
    elif profundidad < 15:
        return minimaxAchi(tablero, profundidad, minMax)

    # Si sobrepaso un límite de tiros, gana el oponente
    return GANA_O if minMax == MAX else GANA_X

def minimaxAchi(tablero, profundidad, minMax):
    # Verificar si ya hay un resultado final
    resultado = esTerminal(tablero)
    if resultado is not None:
        return resultado

    if minMax == MAX:
        # Maximizar el resultado
        mejor = -INFINITO
        mejorMovimiento = (None, None)
        casillaVacia = obtenerCasillaVacia(tablero)
        for i, j in obtenerAdyacencias(tablero, casillaVacia, X):
            nuevoTablero = deepcopy(tablero)
            realizarMovimiento(nuevoTablero, casillaVacia, (i,j))
            resultado = minimax(nuevoTablero, profundidad+1, MIN)
            if resultado > mejor:
                mejor = resultado
                mejorMovimiento = (i, j)

        if mejorMovimiento[0] == None: # Si no es posible realizar un movimiento, es empate
            return EMPATE
        realizarMovimiento(tablero, casillaVacia, mejorMovimiento)
        return mejor
    else:
        # Minimizar el resultado
        mejor = INFINITO
        mejorMovimiento = (None, None)
        casillaVacia = obtenerCasillaVacia(tablero)
        for i, j in obtenerAdyacencias(tablero, casillaVacia, O):
            nuevoTablero = deepcopy(tablero)
            realizarMovimiento(nuevoTablero, casillaVacia, (i,j))
            resultado = minimax(nuevoTablero, profundidad+1, MAX)
            if resultado < mejor:
                mejor = resultado
                mejorMovimiento = (i, j)

        if mejorMovimiento[0] == None: # Si no es posible realizar un movimiento, es empate
            return EMPATE
        realizarMovimiento(tablero, casillaVacia, mejorMovimiento)
        return mejor

def minimaxGato(tablero, profundidad, minMax):
    # import ipdb; ipdb.set_trace()
    # Verificar si ya hay un resultado final
    resultado = esTerminal(tablero)
    if resultado is not None:
        return resultado

    if minMax == MAX:
        # Maximizar el resultado
        mejor = -INFINITO
        mejorMovimiento = (None, None)
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == VACIO:
                    nuevoTablero = deepcopy(tablero)
                    nuevoTablero[i][j] = X
                    resultado = minimax(nuevoTablero, profundidad+1, MIN)
                    if resultado > mejor:
                        mejor = resultado
                        mejorMovimiento = (i, j)
        tablero[mejorMovimiento[0]][mejorMovimiento[1]] = X
        return mejor
    else:
        # Minimizar el resultado
        mejor = INFINITO
        mejorMovimiento = (None, None)
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == VACIO:
                    nuevoTablero = deepcopy(tablero)
                    nuevoTablero[i][j] = O
                    resultado = minimax(nuevoTablero, profundidad+1, MAX)
                    if resultado < mejor:
                        mejor = resultado
                        mejorMovimiento = (i, j)
        tablero[mejorMovimiento[0]][mejorMovimiento[1]] = O
        return mejor

def jugarAchi():
    tablero = [
        [VACIO, VACIO, VACIO],
        [VACIO, VACIO, VACIO],
        [VACIO, VACIO, VACIO]
    ]
    profundidad = 0
    while esTerminal(tablero) == None:
        imprimirTablero(tablero)
        # Pedir tiro de la persona
        i = int(input('Dame el renglon:'))
        j = int(input('Dame la columna:'))
        # Agregar validación!!!
        if profundidad < 8:
            tablero[i][j] = X
        else:
            realizarMovimiento(tablero, (i,j), obtenerCasillaVacia(tablero))
        profundidad += 1
        imprimirTablero(tablero)
        # Pedir tiro de la computadora
        minimax(tablero, profundidad, MIN)
        profundidad += 1

    # Mostrar resultado
    resultado = esTerminal(tablero)
    if resultado == GANA_X:
        print("Ganaste!!!")
    elif resultado == GANA_O:
        print("Perdiste!!!")
    elif resultado == EMPATE:
        print("Ha sido un empate")

####################################################################
jugarAchi()
