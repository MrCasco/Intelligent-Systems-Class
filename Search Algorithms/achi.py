from copy import deepcopy

VACIO, X, O = " ", "X", "O"
MAX, MIN = "max", "min"
GANA_X, GANA_O, EMPATE = 1, -1, 0
INFINITO = 1000

def imprimirTablero(tablero):
    pass

def esTerminal(tablero):
    """
    Revisar si ha ganado algún jugador o si hay empate.
    Si el tablero no es terminal, regresa None
    """
    win = lambda a, b, c: a == b == c
    # Horizontal wins
    if win(tablero[0][0], tablero[0][1], tablero[0][2]):
        return tablero[0][0]
    # Vertical wins
    elif win(tablero[0][0], tablero[1][0], tablero[2][0]):
        return tablero[0][0]
    # Crossed wins
    if win(tablero[0][0], tablero[1][1], tablero[2][2]):
        return tablero[0][0]
    elif win(tablero[0][2], tablero[1][1], tablero[2][0]):
        return tablero[0][2]
    return None



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
                    nuevoTablero[i][j] = "X"
                    resultado = minimax(nuevoTablero, profundidad+1, MIN)
                    if resultado > mejor:
                        mejor = resultado
                        mejorMovimiento = (i, j)
        tablero[mejorMovimiento[0]][mejorMovimiento[1]] = "X"
        return mejor
    else:
        # Minimizar el resultado
        mejor = INFINITO
        mejorMovimiento = (None, None)
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == VACIO:
                    nuevoTablero = deepcopy(tablero)
                    nuevoTablero[i][j] = "O"
                    resultado = minimax(nuevoTablero, profundidad+1, MAX)
                    if resultado < mejor:
                        mejor = resultado
                        mejorMovimiento = (i, j)
        tablero[mejorMovimiento[0]][mejorMovimiento[1]] = "O"
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
        profundidad += 1
        imprimirTablero(tablero)
        # Pedir tiro de la computadora
        minimax(tablero, profundidad, MIN)
        profundidad += 1

    # Mostrar resultado
