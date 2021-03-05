from copy import deepcopy

VACIO, X, O = " ", "X", "O"
MAX, MIN = "max", "min"
GANA_X, GANA_O, EMPATE = 1, -1, 0
INFINITO = 1000

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

def minimax(tablero, profundidad, minMax):
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
        tablero[i][j] = 'X'
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
