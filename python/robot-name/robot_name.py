import random
import string
import time


class Robot(object):
    def __init__(self):
        self.name = self._generate_name()

    def _generate_name(self):
        name = ""
        for i in range(2):
            random.seed(time.time())
            name += random.choice(string.ascii_uppercase)
        for i in range(3):
            random.seed(time.time())
            name += random.choice(string.digits)
        return name

    def reset(self):
        self.name = self._generate_name()
