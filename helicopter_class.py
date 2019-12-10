from Aircraft_class import *

class Helicopter(Aircraft):
    def __init__(self, name, helicopter_number):
        super().__init__(name)
        self.helicopter_number = helicopter_number