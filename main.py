from PIL import Image
import sys

if len(sys.argv) < 2:
    print("Usage: python main.py path/to/image.jpg")
    sys.exit(1)

image_path = sys.argv[1]
img = Image.open("images/" + image_path).convert("L")

img_width, img_height = img.size
ascii_chars = "@%#*+=-:. "

# take avg brightness of pixels in a tile
def tile_to_ascii(tile):
    pixels = list(tile.getdata())
    brightness = sum(pixels)
    avg_brightness = brightness / (len(pixels))

    scale = len(ascii_chars) - 1
    char = ascii_chars[int(avg_brightness / 255 * scale)]
    return char

# idfk how, but it does the job so w/e
def rotate_ascii_image_clockwise(ascii_image_rows):
    return [''.join(row) for row in zip(*ascii_image_rows[::-1])]

ascii_image = []

# divide whole image to tiles
for i in range(0, img_width, img_width // 80):
    row = ""
    for j in range(0, img_height, img_height // 40):
        left = i
        up = j
        right = i + img_width // 40
        down = j + img_height // 40

        tile = img.crop((i, j, right, down))
        row += tile_to_ascii(tile)
    ascii_image.append(row)

# ascii image, correct orientation
rotated_ascii = rotate_ascii_image_clockwise(ascii_image)

# print
for row in rotated_ascii:
    print(row)