INFINITO = 10000

def getFullPath(tabla, start, dest):
    res = [dest]
    node = dest
    while node != start:
        res.append(tabla[node][0])
        node = tabla[node][0]
    return res[::-1]

def pop_min(queue, tabla):
    n = ''
    minimum = INFINITO
    for node in queue:
        if tabla[node][1] < minimum:
            n = node
            minimum = tabla[node][1]
    if n == '':
        return (queue[0], 0)
    return (n, minimum)

def ucs(adjacencies, src, dest):
    # Inicialización
    tabla = {}
    Q = [dest]
    for nodo in adjacencies.keys():
        tabla[nodo] = [None, INFINITO]
        Q.append(nodo)
    tabla[src] = [None, 0]
    tabla[dest] = [None, INFINITO]
    cur = src
    while cur != dest:
        # import ipdb; ipdb.set_trace()
        cur, du = pop_min(Q, tabla)
        Q.pop(Q.index(cur))
        print(cur, tabla[cur])
        if cur == dest:
            print('Path was found', getFullPath(tabla, src, dest), 'with a cost of:', du)
            break
        for child, cost in adjacencies[cur]:
            if du+cost < tabla[child][1]:
                tabla[child] = [cur, du+cost]

adjacencies = {
    's': [('a', 1), ('b', 3), ('e', 5)],
    'a': [('d', 5), ('d', 1)],
    'b': [('c', 2), ('g', 3)],
    'c': [('h', 3), ('b', 2)],
    'd': [('i', 1), ('j', 2)],
    'e': [('f', 1), ('k', 2)],
    'f': [('h', 4)],
    'g': [('h', 1), ('h', 1)],
    'h': [('t', 1)],
    'i': [('k', 1)],
    'j': [('k', 1)],
    'k': [('l', 3)],
    'l': [('t', 2)]
}

adjacencies1 = {
    'a': [('i', 20), ('c', 8), ('d', 1)],
    'b': [('e', 1)],
    'c': [('o', 2)],
    'd': [('e', 10)],
    'e': [('h', 5), ('g', 14), ('d', 10), ('f', 7)],
    'f': [('e', 7), ('k', 4), ('n', 9), ('j', 3)],
    'g': [('l', 18), ('m', 5), ('e', 14)],
    'h': [('m', 2), ('p', 4), ('e', 5), ('g', 1)],
    'i': [('a', 20)],
    'j': [('f', 3), ('o', 24)],
    'k': [('p', 8), ('r', 5), ('f', 4)],
    'l': [('g', 18)],
    'n': [('k', 22), ('f', 9)],
    'm': [('g', 5), ('h', 2)],
    'o': [('c', 2), ('j', 24)],
    'p': [('q', 7), ('h', 4), ('k', 8), ('r', 2)],
    'q': [('p', 7)],
    'r': [('p', 2), ('k', 5), ('s', 3)],
    's': [('r', 3)]
}

ucs(adjacencies, 'a', 't')
