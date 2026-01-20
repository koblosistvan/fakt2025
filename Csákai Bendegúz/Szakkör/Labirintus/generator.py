import random
WALL = '#'
PATH = ' '

# -----------------------------
# Disjoint Set (Union-Find)
# -----------------------------
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True


# -----------------------------
# Kruskal Maze Generator
# -----------------------------
def generate_kruskal_maze(width=41, height=41, seed=None):
    if seed is not None:
        random.seed(seed)

    # Ensure odd dimensions for proper walls
    if width % 2 == 0:
        width -= 1
    if height % 2 == 0:
        height -= 1

    # Initialize grid full of walls
    maze = [[WALL] * width for _ in range(height)]

    # Cell positions (odd coordinates)
    cells = []
    cell_index = {}
    idx = 0
    for y in range(1, height, 2):
        for x in range(1, width, 2):
            cells.append((x, y))
            cell_index[(x, y)] = idx
            idx += 1
            maze[y][x] = PATH

    dsu = DisjointSet(len(cells))

    # List of walls between cells
    walls = []
    for x, y in cells:
        for dx, dy in [(2, 0), (0, 2)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in cell_index:
                walls.append(((x, y), (nx, ny)))

    random.shuffle(walls)

    # Kruskal's algorithm
    for (x1, y1), (x2, y2) in walls:
        c1 = cell_index[(x1, y1)]
        c2 = cell_index[(x2, y2)]
        if dsu.union(c1, c2):
            wx = (x1 + x2) // 2
            wy = (y1 + y2) // 2
            maze[wy][wx] = PATH

    maze[0][maze[1].index(PATH)] = PATH
    return ["".join(row) for row in maze]


# -----------------------------
width, height, seed = 41, 41, 42
path = '_Megoldások\\Szakkör\\Labirintus\\'
maze = generate_kruskal_maze(width, height, seed)
with open(path + f'labirintus-{seed}-{width}x{height}.txt', mode='w', encoding='utf-8') as f:
    print(f'{width} {height}', file=f)
    [print(line, file=f) for line in maze]
