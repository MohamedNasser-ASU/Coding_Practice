import sys
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    sys.exit("Too few command-line arguments")
elif not ((sys.argv[1].lower().endswith("png") and sys.argv[2].lower().endswith("png"))
or (sys.argv[1].lower().endswith("jpg") and sys.argv[2].lower().endswith("jpg"))
or (sys.argv[1].lower().endswith("jpeg") and sys.argv[2].lower().endswith("jpeg"))):
    sys.exit("Invalid input")

try:
    shirt = Image.open("shirt.png")
    image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Invalid")
else:
    image = ImageOps.fit(image,[600,600])
    image.paste(shirt,shirt)
    image.save(sys.argv[2])

