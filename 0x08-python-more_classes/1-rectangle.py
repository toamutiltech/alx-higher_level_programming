#!/usr/bin/python3
class Rectange:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        @property
        def width(self):
            print("to retrive the width")

            return self.__width

        @width.setter
        def width(self, value):
            try:
                value.isdigit():
                self.__width = value
            except TypeError:
                print("width must be an integer")
            except ValueError:
                print("width must be >= 0")

        @property
        def height(self):
            print("to retrive the height")
            
            return self.__height

        @height.setter
        def height(self, value):
            try:
                value.isdigit():
                self.__height = value
            except TypeError:
                print("height must be an integer")
            except ValueError:
                print("height must be >= 0")


