from PIL import Image
import numpy as np

# Deprecated
def calculate_new_positions(x, y, radius):
    factor = radius
    return {
        'top': [x ,y -radius],
        'bottom': [x, y + radius],
        'left': [x - radius, y],
        'right': [x + radius, y],
        'top_left': [x -radius, y-radius],
        'bottom_left': [x-radius, y+radius],
        'top_right': [x+radius,y-radius],
        'bottom_right': [x+radius,y+radius]
    }


def extract_submatrix(x, y, height, width, image_data, radius, weight):
    x_min = x - radius
    # The plus one (+1) is to also include the last element
    x_max = x + radius + 1
    y_min = y - radius
    y_max = y + radius + 1

    # Boundary conditions
    if x_min < 0:
        x_min = 0
    elif x_max > width:
        x_max = width - 1
    if y_min < 0:
        y_min = 0
    elif y_max > height:
        y_max = height - 1

    # Multiplies the center pixel by the weight
    image_data[y][x] = image_data[y][x]*weight

    submatrix = image_data[y_min:y_max, x_min:x_max]
    height, width, last = submatrix.shape

    return submatrix, height, width


def save_new_image(data, name):
    im2 = Image.fromarray(data.astype('uint8'))
    im2.save(name)


def open_image(image):
    try:
        img = Image.open(image)
        img = img.convert('RGBA')
        width, height = img.size
    except :
        exit('Por favor, informe uma imagem válida.')

    return img, width, height


def get_image_data(image):
    return np.array(image).astype('int64')


def calculate_new_color(image_data, weight, height, width):
    rgba_sum = np.sum(image_data, axis=(1, 0))

    denominator = (height * width - 1) + weight

    new_color = np.round(rgba_sum / denominator)

    return new_color

