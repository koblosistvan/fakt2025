bemenet_1 = [7, 25]
bemenet_2 = [
    '.#...#....#....#.....#...',
    '#.#..#...#.#...#....#.#..',
    '.#...#..#...#..#...#...#.',
    '.....#...#.#...#..#.....#',
    '.....#....#....#...#...#.',
    '.....#.........#....#.#..',
    '.....#.........#.....#...',
]

m, sz = bemenet_1
def gyemant_e(x, y):
    magassag = 1
    while bemenet_2[y + magassag][x - magassag : x + magassag + 1] == '#' + '.'*(magassag-1) + '.#':
        magassag += 1
    if magassag == 1:
        return False
    else:
        while bemenet_2[y + magassag][x - magassag : x + magassag + 1] == '#' + '.'*(magassag-1) + '.#':
            magassag += 1
    
        


gyemantok = 0
for y in range(m):
    for x in range(sz):
        if gyemant_e(x, y):
            gyemantok += 1

print(gyemantok)