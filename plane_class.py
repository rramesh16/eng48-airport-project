from Aircraft_class import *

class Plane():
    def __init__(self, plane_number):
        # super().__init__(name)
        self.plane_number = plane_number

    def add_plane_number(self, plane_no):
        new_plane_number = self
        new_plane_number.plane_number.append(plane_no)
