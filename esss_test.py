from sys import argv
from tasks import create_blur_image, change_image_color

if len(argv) == 5 and argv[1] == '-blur':
    try:
        create_blur_image(argv[2], int(argv[3]), int(argv[4]))
    except NameError:
        exit('Please enter valid integers for radius and weight')

elif len(argv) == 3 and argv[1] == '-rgb':
    change_image_color(argv[2])
else:
    print('Available commands: \n '
          'python esss_test.py -blur <image-file> <radius> <weight>\n '
          'python esss_test.py -rgb <image-file>')



