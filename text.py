# -*- coding: utf-8 -*-

from GUI.initialisation import *
from GUI.color import Color

class Text:
    def __init__(
            self,
            text: str,
            size: int,
            font: str | None=None,
            color: tuple=(0,0,0)
        ) -> None:
        """A class that represents a text object that can be displayed on the screen.

        Args:
            - text (str): The text to display.
            - size (int): The font size.
            - font (str | None, optional): The font to use for the text. Defaults to None.
            - color (tuple, optional): The color of the text. Defaults to (0, 0, 0).
        """
        self.__text = text
        self.__size = resize(size)
        self.__color = Color(*color)
        self.__font_name = font
        self.__change_surface()

    def __change_surface(self) -> None:
        """Private method to update the surface with the new text, size, color and font."""
        self.__font = pygame.sysfont.SysFont(self.__font_name, self.__size)
        self.__surface = self.__font.render(self.__text, True, self.__color)

    def draw(
            self,
            surface: pygame.Surface,
            pos: tuple | list
        ) -> None:
        """Draws the text object onto a surface.

        Args:
            - surface (pygame.Surface): The surface to draw onto.
            - pos (tuple | list): The position to draw the text at.
        """
        size = self.__surface.get_size()
        pos = resize(pos[0]) - size[0] / 2, resize(pos[1]) - size[1] / 2
        surface.blit(self.__surface, pos)
    
    def get_rect(self, **kwargs) -> pygame.Rect:
        """Get the rectangular area of the text surface.

        Returns:
            - pygame.Rect: The rectangular area of the text surface.
        """
        return self.__surface.get_rect(**kwargs)


    @property
    def text(self) -> str:
        """The text value."""
        return self.__text
    @text.setter
    def text(self, value: str) -> None:
        self.__text = value
        self.__change_surface()

    @property
    def size(self) -> int:
        """The font size."""
        return self.__size
    @size.setter
    def size(self, value: int) -> None:
        self.__size = resize(value)
        self.__change_surface()

    @property
    def color(self) -> Color:
        """The text color."""
        return self.__color.copy()
    @color.setter
    def color(self, value: tuple) -> None:
        self.__color = Color(*value)
        self.__change_surface()

    @property
    def font(self) -> str | None:
        """The font name"""
        return self.__font_name
    @font.setter
    def font(self, value: str) -> None:
        self.__font_name = value
        self.__change_surface()

if __name__ == "__main__":
    from random import randint
    titre = Text("salut", 50, "arial", (255, 255, 255))
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        titre.draw(screen, (100, 100))
        color = randint(100, 255), randint(100, 255), randint(100, 255)
        size = randint(10, 100)
        titre.color = color
        titre.size = size
        

        pygame.display.flip()
        clock.tick(60)
        