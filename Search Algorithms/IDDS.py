from copy import deepcopy

def move_piece(board, direction, zero):
    if direction == 'up':
        board[zero[0]][zero[1]], board[zero[0]-1][zero[1]] = board[zero[0]-1][zero[1]], board[zero[0]][zero[1]]
    elif direction == 'down':
        board[zero[0]][zero[1]], board[zero[0]+1][zero[1]] = board[zero[0]+1][zero[1]], board[zero[0]][zero[1]]
    elif direction == 'right':
        board[zero[0]][zero[1]], board[zero[0]][zero[1] + 1] = board[zero[0]][zero[1]+1], board[zero[0]][zero[1]]
    elif direction == 'left':
        board[zero[0]][zero[1]], board[zero[0]][zero[1] -1] = board[zero[0]][zero[1]-1], board[zero[0]][zero[1]]
    res = ';'.join([' '.join(board[x]) for x in range(3)])
    return res


def possible_moves(_board):
    res = []
    zero_index = (0, 0)
    board = _board
    _board = []
    for row in board.split(';'):
        _board.append(row.split(' '))
    for i in range(len(_board)):
        if '0' in _board[i]:
            zero_index = (i, _board[i].index('0'))
    for move in moves[zero_index]:
        yield move_piece(deepcopy(_board), move, zero_index)


def idds(src, goal, limit):
    visitados_src = {}
    stack_src = [src]
    visitados_src[src] = 1
    height=0
    i = 0
    while i<18441: #stack_src:
        # import ipdb; ipdb.set_trace()
        i+=1
        # Sacar del stack dependiendo de profundidad no del último en meterse al stack
        if src == goal:
            print('We have finished after', i, 'movements')
            stack_src.clear()
            break
        for child in possible_moves(src):
            # Meter al stack los posibles movimientos
            #Si no encuentra los posibles hijos en visitado hacer dfs
            if child == goal:
                return 'webos'
            if visitados_src.get(child)== None:
                stack_src.append(child)
                print('Holaa', i)
                print(stack_src)
                if i != limit and i<height:
                    return idds(stack_src.pop(0), goal, limit+1)
    return 'Not solvable'


source = '1 2 3;0 4 6;7 5 8'
# source = '1 2 3;4 5 6;7 0 8'
solution = '1 2 3;4 5 6;7 8 0'


moves = {
    (0, 0): ['down', 'right'],
    (0, 1): ['down', 'right', 'left'],
    (0, 2): ['down', 'left'],
    (1, 0): ['down', 'right', 'up'],
    (1, 1): ['down', 'right', 'left', 'up'],
    (1, 2): ['down', 'left', 'up'],
    (2, 0): ['up', 'right'],
    (2, 1): ['up', 'right', 'left'],
    (2, 2): ['up', 'left'],
}

print(idds(source, solution, 0))
