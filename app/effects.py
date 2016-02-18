import os
import time
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.conf import settings
from PIL import Image, ImageFilter, ImageOps, ImageEnhance
from models import Effect


class EditImage:

    def __init__(self, image, effect):
        self.filename = os.path.basename(image)
        path = os.path.dirname(image) + '/edited/' + str(effect)
        if not os.path.exists(path):
            os.makedirs(path)

        self.temp_dir = path
        self.image = Image.open(image)
        self.effect = effect
        self.new_file = self.temp_dir + '/' + self.filename

    def enhancements(self, enhancement):

        enhancer = ImageEnhance.Contrast(self.image)
        self.image = enhancer.enhance(enhancement['contrast'])

        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(enhancement['brightness'])

        enhancer = ImageEnhance.Sharpness(self.image)
        self.image = enhancer.enhance(enhancement['sharpness'])

        enhancer = ImageEnhance.Color(self.image)
        self.image = enhancer.enhance(enhancement['color'])

        alt_name = self.temp_dir + '/' + str(time.time()).translate(None, '.') + self.filename

        if os.path.exists(alt_name):
            os.remove(alt_name)
            alt_name = self.temp_dir + '/' + str(time.time()).translate(None, '.') + self.filename
        self.new_file = alt_name

        self.image.save(self.new_file)
        return self.effect + '/' + os.path.basename(self.new_file)

    def operations(self):
        if self.effect == 'flip':
            to_save = ImageOps.flip(self.image)

        if self.effect == 'mirror':
            to_save = ImageOps.mirror(self.image)
        if self.effect == 'grayscale':
            to_save = ImageOps.grayscale(self.image)
        to_save.save(self.new_file)
        return self.effect + '/' + os.path.basename(self.new_file)

    def filters(self):
        if self.effect == 'smooth':
            to_save = self.image.filter(ImageFilter.SMOOTH)
        if self.effect == 'emboss':
            to_save = self.image.filter(ImageFilter.EMBOSS)
        if self.effect == 'contour':
            to_save = self.image.filter(ImageFilter.CONTOUR)
        if self.effect == 'sharpen':
            to_save = self.image.filter(ImageFilter.SHARPEN)
        if self.effect == 'findedges':
            to_save = self.image.filter(ImageFilter.FIND_EDGES)
        if self.effect == 'blur':
            to_save = self.image.filter(ImageFilter.BLUR)
        to_save.save(self.new_file)
        return self.effect + '/' + os.path.basename(self.new_file)

    def basic_effects(self):
        if self.effect == 'rotate':
            to_save = self.image.rotate(angle)
        to_save.save(self.new_file)
        return self.effect + '/' + os.path.basename(self.new_file)
