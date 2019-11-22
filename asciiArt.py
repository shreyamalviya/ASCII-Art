from PIL import Image
from sty import Style, RgbFg
from sty import fg
import fire


def fullColor(imgHeight, imgWidth, pixels):
    char = '█'
    for row in range(imgHeight):
        for col in range(imgWidth):
            fg.col = Style(RgbFg(pixels[col, row][0],
                                 pixels[col, row][1],
                                 pixels[col, row][2]))
            print(fg.col + char + fg.rs, end='')
            print(fg.col + char + fg.rs, end='')
        print()

def coloredASCII(imgHeight, imgWidth, pixels):
    ASCII = "`^\",:;Il!i~+-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    for row in range(imgHeight):
        for col in range(imgWidth):
            bright = round(sum(pixels[col, row])/3)
            char = bright//4
            fg.col = Style(RgbFg(pixels[col, row][0],
                                 pixels[col, row][1],
                                 pixels[col, row][2]))
            print(fg.col + ASCII[char] + fg.rs, sep='', end='')
            print(fg.col + ASCII[char] + fg.rs, sep='', end='')
        print()

def bwASCII(imgHeight, imgWidth, pixels):
    ASCII = "`^\",:;Il!i~+-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    for row in range(imgHeight):
        for col in range(imgWidth):
            bright = round(sum(pixels[col, row])/3)
            char = bright//4
            print(ASCII[char], end='')
            print(ASCII[char], end='')
        print()


def editPhoto(photoPath, style):
    """ 
    Edit your photos, terminal style!
    Styles:
        1 - full color;
        2 - colored ASCII;
        3 - black & white ASCII
    """
    img = Image.open(photoPath)
    imgWidth, imgHeight = img.size 
    img = img.resize((round(imgWidth/3), round(imgHeight/3)))
    imgWidth, imgHeight = img.size 
    pixels = img.load()
    
    if style == 1:
        fullColor(imgHeight, imgWidth, pixels)
    elif style == 2:
        coloredASCII(imgHeight, imgWidth, pixels)
    elif style == 3:
        bwASCII(imgHeight, imgWidth, pixels)

if __name__ == '__main__':
    fire.Fire(editPhoto)
