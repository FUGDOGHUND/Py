import math
import matplotlib.pyplot as plt
import numpy as np

def julia_fractal(c, max_iter, width, height):
    zx, zy = np.meshgrid(np.linspace(-1, 1, width), np.linspace(-1, 1, height))
    img = np.zeros((width, height))
    for i in range(max_iter):
        zx2 = zx ** 2
        zy2 = zy ** 2
        mask = zx2 + zy2 < 4
        img[mask] = i
        zy[mask], zx[mask] = 2 * zx[mask] * zy[mask] + c.imag, zx2[mask] - zy2[mask] + c.real
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


#NumPy версия скорее всего
#будет значительно быстрее за счет векторизации операций и эффективного использования памяти
#По моему мнению