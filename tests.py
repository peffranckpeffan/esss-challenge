import unittest
import tasks

class TestTasks(unittest.TestCase):

    def test_blur(self):
        tasks.create_blur_image('test-image.png', 5, 100)

    def test_rgb(self):
        tasks.change_image_color('test-image.png')