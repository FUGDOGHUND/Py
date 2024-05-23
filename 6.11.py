import math
import matplotlib.pyplot as plt
import numpy as np

def julia_fractal(c, max_iter, width, height):
    img = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            zx = 3 * (x - width/2) / (width/2)  # Normalize x coordinate
            zy = 2 * (y - height/2) / (height/2)  # Normalize y coordinate
            i = 0
            while zx*zx + zy*zy < 4 and i < max_iter:
                xtemp = zx*zx - zy*zy + c.real
                zy = 2*zx*zy + c.imag
                zx = xtemp
                i += 1
            img[x, y] = i
    return img

# Параметры
max_iter = 255
width, height = 800, 800
c = complex(-0.8, 0.156)

# Создание фрактала Жюлиа
fractal_img = julia_fractal(c, max_iter, width, height)

# Отображение фрактала
plt.imshow(fractal_img.T, cmap='hot', interpolation='bilinear', origin='lower')
plt.axis('off')
plt.show()