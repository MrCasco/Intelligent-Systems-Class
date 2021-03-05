maze1 = [
"**********",
"*S    ** *",
"*****    *",
"**    ** *",
"***** ****",
"*****   E*",
"**********"
]

maze2 = [
"**********",
"*S    ** *",
"* ***    *",
"*     ** *",
"***** ****",
"*****   E*",
"**********"
]

def get_full_path(padres):
    p = (8, 4)
    res = [p]
    while p != (1, 0):
        p = padres[p[0]][p[1]]
        res.append(p)
    return res[::-1]

def neighbors(node, maze):
    x = node[0]
    y = node[1]
    ns = []
    if (x-1 >= 0) and (maze[y][x-1] == ' ' or maze[y][x-1] == 'E'):
        ns.append((x-1, y))
    if (x+1 < 9) and (maze[y][x+1] == ' ' or maze[y][x+1] == 'E'):
        ns.append((x+1, y))
    if (y-1 >= 0) and (maze[y-1][x] == ' ' or maze[y-1][x] == 'E'):
        ns.append((x, y-1))
    if (y+1 < 5) and (maze[y+1][x] == ' ' or maze[y+1][x] == 'E'):
        ns.append((x, y+1))
    return ns

def dfs(maze):
    visitados = [[0 for i in range(len(maze)-2)] for _ in range(len(maze[0])-1)]
    visitados[1][0] = 1
    padres = [[0 for i in range(len(maze)-2)] for _ in range(len(maze[0])-1)]
    stack = [(1, 0)]
    DESTINO = (8, 4)
    while stack:
        n = stack.pop()
        for nx, ny in neighbors(n, maze[1:]):
            if visitados[nx][ny] == 0:
              visitados[nx][ny] = 1
              stack.append((nx, ny))
              padres[nx][ny] = (n[0], n[1])
              if (nx, ny) == DESTINO:
                  print('This is the path taken (x, y):', get_full_path(padres))
                  stack.clear()
                  break

dfs(maze1)
dfs(maze2)
