# -*- coding: utf-8 -*-

from GUI.initialisation import *

class Color(pygame.color.Color):

    def __init__(self, r: int, g: int, b: int, a: int=255) -> None:
        super().__init__(r, g, b, a)
        self.__initial_r = r
        self.__initial_g = g
        self.__initial_b = b
        self.__initial_a = a
    
    def lighten(self, additive_percentage: float) -> "Color":
        """lighten the color by the given percentage

        Args:
            - additive_percentage (float): the percentage by which to lighten between 0 and 100

        Returns:
            - Color: the new color
        """
        self.r += round(((255 - self.r)/100) * additive_percentage)
        self.g += round(((255 - self.g)/100) * additive_percentage)
        self.b += round(((255 - self.b)/100) * additive_percentage)
        return self
    
    def lighten_values(self, r: float, g: float, b: float) -> "Color":
        """lighten the value of each r,g,b values by the given percentage 

        Args:
            - r (float): the change for the `r` value between 0 and 100
            - g (float): the change for the `g` value between 0 and 100
            - b (float): the change for the `b` value between 0 and 100

        Returns:
            - Color: the new color
        """
        self.r += round(((255 - self.r)/100) * r)
        self.g += round(((255 - self.g)/100) * g)
        self.b += round(((255 - self.b)/100) * b)
        return self
    

    def darken(self, subtractive_percentage: float) -> "Color":
        """darken the color by the given percentage

        Args:
            - subtractive_percentage (float): the percentage by which to darken between 0 and 100

        Returns:
            - Color: the new color
        """
        self.r = round((self.r/100) * (100-subtractive_percentage))
        self.g = round((self.g/100) * (100-subtractive_percentage))
        self.b = round((self.b/100) * (100-subtractive_percentage))
        return self
    
    def darken_values(self, r: float, g: float, b: float) -> "Color":
        """darken the value of each r,g,b values by the given percentage 

        Args:
            - r (float): the change for the `r` value between 0 and 100
            - g (float): the change for the `g` value between 0 and 100
            - b (float): the change for the `b` value between 0 and 100

        Returns:
            - Color: the new color
        """
        self.r = round((self.r/100) * (100-r))
        self.g = round((self.g/100) * (100-g))
        self.b = round((self.b/100) * (100-b))
        return self
    
    def change_color(self, percentage: float) -> "Color":
        """change the color by the given percentage
        if the given number is negative darken the value, if it's positive, it will lighten it

        Args:
            - percentage (float): the change of the color between -100 and 100

        Returns:
            - Color: the new color
        """
        if percentage < 0: self.darken(abs(percentage))
        elif percentage > 0: self.lighten(percentage)

        return self
    
    def change_color_values(self, r: float, g: float, b: float) -> "Color":
        """chage the value of each r,g,b values by the given percentage 
        if the given number is negative darken the value, if it's positive, it will lighten it

        Args:
            - r (float): the change for the `r` value between -100 and 100
            - g (float): the change for the `g` value between -100 and 100
            - b (float): the change for the `b` value between -100 and 100

        Returns:
            - Color: the new color
        """
        if r < 0: self.darken_values(abs(r), 0, 0)
        elif r > 0: self.lighten_values(r, 0, 0)

        if g < 0: self.darken_values(0, abs(g), 0)
        elif g > 0: self.lighten_values(0, g, 0)

        if b < 0: self.darken_values(0, 0, abs(b))
        elif b > 0: self.lighten_values(0, 0, b)

        return self

    def restor_color(self) -> "Color":
        """reset the r,g,b,a values of the color to there initial values

        Returns:
            - Color: the new color
        """
        self.r = self.__initial_r
        self.g = self.__initial_g
        self.b = self.__initial_b
        self.a = self.__initial_a
        return self
    
    def copy(self) -> "Color":
        """copy the color

        Returns:
            - Color: the copy of the color
        """
        return Color(self.r, self.g, self.b, self.a)


if __name__ == "__main__":
    __color1 = Color(1, 125, 255)
    __color = Color(100, 100, 100)
    print(__color.darken(90))
    print(__color)
    for i in range(5):
        print(__color1)
        __color1.change_color(10)
        print(__color1)
        __color1.change_color(-10)
    print(__color1)