import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def floyd_steinberg_dithering(image):
    height, width = image.shape
    output_image = np.zeros((height, width), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            old_pixel = image[y, x]
            new_pixel = 255 if old_pixel > 128 else 0
            output_image[y, x] = new_pixel
            quant_error = old_pixel - new_pixel

            if x < width - 1:
                image[y, x + 1] += quant_error * 7 / 16
            if y < height - 1:
                image[y + 1, x] += quant_error * 5 / 16
                if x > 0:
                    image[y + 1, x - 1] += quant_error * 3 / 16
                if x < width - 1:
                    image[y + 1, x + 1] += quant_error * 1 / 16

    return output_image


# Загрузка изображения и преобразование в массив NumPy
image = Image.open('11.png').convert('L')
image_array = np.array(image)

# Применение алгоритма Флойда-Стейнберга
output_image = floyd_steinberg_dithering(image_array)

# Преобразование результата обратно в изображение
output_image = Image.fromarray(output_image)

# Отображение изображения
plt.imshow(output_image, cmap='gray')
plt.axis('off')
plt.show()