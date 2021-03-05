def contar(padres):
    print(list(zip([i for i in range(25)], padres)))
    p = 25
    tiros = 0
    while p != 0:
        p = padres[p]
        tiros += 1
    return tiros

def adyacencias(n, tab):
    # retornar lista de los nodos hijo de n
    return tab[n]

# BFS
def bfs(nodo_inicial, tablero):
    NO_VISITADO, VISITADO = 0, 1
    DESTINO = 25
    queue = [nodo_inicial] #Agrego el nodo inicial
    visitados = [NO_VISITADO for _ in range(26)]
    padres = [None for _ in range(26)]
    res = [nodo_inicial]

    while queue:
        n = queue.pop(0)
        for nodo in adyacencias(n, tablero):
            if visitados[nodo] == NO_VISITADO:
                padres[nodo] = n
                visitados[nodo] = VISITADO
                queue.append(nodo)
                if nodo == DESTINO:
                    # Ya llegué a la meta!
                    # Contar el número de acciones realizadas
                    acciones = contar(padres)
                    # Mostrar resultado y terminar ejecución
                    print('El número de tiros es:', acciones)

tablero = [[] for _ in range(26)]

for i in range(19):
    tablero[i] = [i+1, i+2, i+3, i+4, i+5, i+6]

tablero[20] = [21, 22, 23, 24, 25]
tablero[21] = [22, 23, 24, 25]
tablero[22] = [23, 24, 25]
tablero[23] = [24, 25]
tablero[24] = [25]

TIRO_1, TIRO_2, TIRO_3, TIRO_4, TIRO_5, TIRO_6 = 0,1,2,3,4,5
# Escaleras
# Escalera 3->14
tablero[0][TIRO_3] = 14
tablero[1][TIRO_2] = 14
tablero[2][TIRO_1] = 14
# Escalera 12->18
tablero[6][TIRO_6] = 18
tablero[7][TIRO_5] = 18
tablero[8][TIRO_4] = 18
tablero[9][TIRO_3] = 18
# tablero[10][TIRO_2] = 18 No se puede
tablero[11][TIRO_1] = 18
# Escalera 16->23
# tablero[10][TIRO_6] = 23 No se puede
tablero[11][TIRO_5] = 23
# tablero[12][TIRO_4] = 23 No se puede
tablero[13][TIRO_3] = 23
tablero[14][TIRO_2] = 23
tablero[15][TIRO_1] = 23
# Serpientes
# Serpiente 10->1
tablero[4][TIRO_6] = 1
tablero[5][TIRO_5] = 1
tablero[6][TIRO_4] = 1
tablero[7][TIRO_3] = 1
tablero[8][TIRO_2] = 1
tablero[9][TIRO_1] = 1
# Serpiente 17->6
tablero[11][TIRO_6] = 6
# tablero[12][TIRO_5] = 6 No se puede
tablero[13][TIRO_4] = 6
tablero[14][TIRO_3] = 6
tablero[15][TIRO_2] = 6
tablero[16][TIRO_1] = 6


##########################
print("A partir de la casilla 6, si tiro un 6: ", tablero[6][TIRO_6])
bfs(0, tablero)
