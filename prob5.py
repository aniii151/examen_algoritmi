#A* la fiecare pas alege nodul cu cea mai mica valoare
#a functiei f(n)= g(n)+h(n)
#gaseste cel mai scurt drum de la un nod de start la un nod tinta


from heapq import heappush, heappop

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])  # distanța Manhattan

def astar(grid, start, goal):
    open_set = [(0, start, [start])]  # (cost total, nod curent, drumul până aici)
    rows, cols = len(grid), len(grid[0])
    visited = set()

    while open_set:
        f, (x, y), path = heappop(open_set)
        if (x, y) == goal:
            return path
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                g = len(path)         # cost drum până acum
                h = heuristic((nx, ny), goal)
                heappush(open_set, (g+h, (nx, ny), path+[(nx, ny)]))
    return []

if __name__ == "_main_":
    grid = [
        [0,0,0],
        [0,1,0],  # obstacol în centru
        [0,0,0]
    ]
    print(astar(grid, (0,0), (2,2)))