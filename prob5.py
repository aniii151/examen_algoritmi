#A* la fiecare pas alege nodul cu cea mai mica valoare
#a functiei f(n)= g(n)+h(n)
#gaseste cel mai scurt drum de la un nod de start la un nod tinta



from heapq import heappush, heappop

Grid = list[list[int]]

def heuristic(a, b):
    (x1, y1), (x2, y2) = a, b
    return abs(x1 - x2) + abs(y1 - y2)

def astar(grid: Grid, start: tuple[int,int], goal: tuple[int,int]):
    # TODO
    return []

if __name__ == "__main__":
    grid = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    print(astar(grid, (0,0), (2,2)))