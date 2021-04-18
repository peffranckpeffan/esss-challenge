from util import open_image, save_new_image, get_image_data, extract_submatrix, calculate_new_color


# TASK 2 and TASK 3
def create_blur_image(image, radius, weight):
    img, width, height = open_image(image)

    image_data = get_image_data(img)

    new_image_data = get_image_data(img)

    new_color = []
    for x in range(width):
        for y in range(height):
            image_data_submatrix, height_sub, width_sub = extract_submatrix(x, y, height, width,
                                                                            image_data.copy(), radius, weight)

            new_color = calculate_new_color(image_data_submatrix, weight, height_sub, width_sub)

            new_image_data[y][x] = new_color

    save_new_image(new_image_data, f'test-image-blur-radius-{radius}-weight-{weight}.png')
    print('Image successfully changed.')


# TASK 1
def change_image_color(image):

    img, width, height = open_image(image)

    image_data = get_image_data(img)

    new_color = []

    for color in ['red', 'green', 'blue']:
        for x in range(width):
            for y in range(height):
                r, g, b, alpha = img.getpixel((x, y))
                if color == 'red':
                    new_color = [r,0,0, alpha]
                elif color== 'green':
                    new_color = [0,g,0, alpha]
                elif color == 'blue':
                    new_color = [0,0,b, alpha]

                image_data[y][x] = new_color

        save_new_image(image_data, f"test-image-split-{color}.png")

    print('Images successfully saved.')