from PIL import Image

import os

class ColorSwitcher:
    def __init__(self, path_to_dataset, path_to_save, special_string, colors_to_switch):
        self.path_to_dataset = path_to_dataset
        self.path_to_save = path_to_save
        self.special_string = special_string
        self.colors_to_switch = colors_to_switch

    def _switch_color_in_file(self, img):
        pixels = img.load()
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if pixels[i, j] in self.colors_to_switch.keys():
                    pixels[i, j] = self.colors_to_switch[pixels[i, j]]

    def switch_color(self):
        for root, dirs, files in os.walk(self.path_to_dataset):
            for file in files:
                if file.endswith(self.special_string):
                    path_to_file = os.path.join(root, file)
                    img = Image.open(path_to_file)
                    img = img.convert('RGB')
                    self._switch_color_in_file(img)
                    img.save(f"{self.path_to_save}/{file}")



