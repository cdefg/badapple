from PIL import Image

char_string = ' #'

def rgb2char(r, g, b):
    length = len(char_string)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length

    idx = int(gray / unit)
    return char_string[idx]

def img2char(img_obj, savepath):
    txt = ''
    width, height = img_obj.size

    for i in range(height):
        line = ''
        for j in range(width):
            line += rgb2char(*img_obj.getpixel((j, i)))
        txt = txt + line + '\n'
    with open(savepath, 'w+', encoding='utf-8') as f:
        f.write(txt)


filenum=2193
for i in range(1,filenum):
    filename=str(i)+'.jpeg'
    img_obj = Image.open(filename)
    img2char(img_obj,str(i)+'.txt')
