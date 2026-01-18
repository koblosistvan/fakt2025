from PIL import Image

source = open(r'Ódor Artúr\python\Fenyőfa\fenyofa.txt', 'r', encoding='utf-8')
width, height = [int(a) for a in source.readline().strip().split()]
pixels = []
for _ in range(height):
    line = source.readline()
    pixels.append(line.rstrip('\n'))

COLORS = {                     # RGBA, az utolsó az átlátszóság
    'h': (0, 0, 0, 0),         # átlátszó háttér
    'z': (0, 150, 0, 255),     # zöld
    'b': (120, 72, 0, 255),    # barna
    's': (255, 215, 0, 255),   # sárga
    'p': (220, 20, 60, 255),   # piros
    'k': (30, 144, 255, 255),  # kék
    'f': (255, 255, 255, 255),  # fehér
    'a': (250, 210, 0, 250)
}

img = Image.new('RGBA', (width, height), (0, 0, 0, 0)) 
for y in range(height):
    for x in range(width):
        img.putpixel((x, y), COLORS[pixels[y][x]])

img.save(r'Ódor Artúr\python\Fenyőfa\fenyofa.png')
print('Elkészült a képfájl.')
