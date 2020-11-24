from perlin_math import PerlinNoiseFactory
import PIL.Image


# Создание шума
def generate_perlin_noise(settings):
    # Размер карты
    size = settings['size']
    # Масштаб
    zoom = settings['zoom']

    space_range = size / zoom

    pnf = PerlinNoiseFactory(2, octaves=8, tile=(space_range, space_range))
    img = PIL.Image.new('RGBA', (size, size))
    for x in range(size):
        for y in range(size):
            n = pnf(x / zoom, y / zoom)
            img.putpixel((x, y), (0, 0, 0, int((n + 1) / 2 * 255 + 0.5)))
    return img


def add_color(img, colors):
    for x in range(img.size[0]):
        for y in range(img.size[0]):
            pixel_data = img.getpixel((x, y))
            for color in colors:
                if color[1]:
                    if colors.index(color) == 0 and color[0] >= pixel_data[3]:
                        img.putpixel((x, y), color[2])
                    elif color[0] >= pixel_data[3] >= lastcolor[0]:
                        img.putpixel((x, y), color[2])
                    elif colors.index(color) + 1 == len(colors) and color[0] <= pixel_data[3]:
                        img.putpixel((x, y), color[2])
                        print(pixel_data[3])
                    lastcolor = color
    return img
