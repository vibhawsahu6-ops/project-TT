from pathlib import Path  
from PIL import Image

# Load image
BASE_DIR = Path(__file__).resolve().parent
img = Image.open(BASE_DIR / "image.jpg")

# Convert image to grayscale (0 = black, 255 = white)
img = img.convert("L")

# Resize for console output
new_width = 120
new_height = int((img.height / img.width) * new_width * 0.42)
img = img.resize((new_width, new_height))


# ASCII characters
ascii_chars = "@%#*+=-:. "
pixels = img.getdata()

# Convert pixels to ASCII
ascii_image = ""

for i in range(len(pixels)):
    brightness = pixels[i]

    # Conditional mapping for 10 ASCII characters
    if brightness < 26:
        ascii_image += ascii_chars[0]
    elif brightness < 52:
        ascii_image += ascii_chars[1]
    elif brightness < 78:
        ascii_image += ascii_chars[2]
    elif brightness < 104:
        ascii_image += ascii_chars[3]
    elif brightness < 130:
        ascii_image += ascii_chars[4]
    elif brightness < 156:
        ascii_image += ascii_chars[5]
    elif brightness < 182:
        ascii_image += ascii_chars[6]
    elif brightness < 208:
        ascii_image += ascii_chars[7]
    elif brightness < 234:
        ascii_image += ascii_chars[8]
    else:
        ascii_image += ascii_chars[9]


    # New line after width
    if (i + 1) % 120 == 0:
        ascii_image += "\n"

print(ascii_image)

'''
Dark pixel   → @
Medium dark  → #*
Medium       → +=
Light        → -:.
Very light   →  
'''