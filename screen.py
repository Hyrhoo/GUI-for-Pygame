# -*- coding: utf-8 -*-

from GUI.initialisation import *

class Screen:

    def __init__(self, size=SCREEN_SIZE) -> None:
        self.screen_size = tuple(resize(i) for i in size)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.scroll_movement = resize(50)
        self.__screen_pos = 0

    def set_scroll_movement(self, scroll: int=0) -> None:
        scroll = resize(scroll)
        self.scroll_movement = scroll

    def scroll(self, mini: int, maxi: int, mov: int) -> None:
        self.__screen_pos += resize(mov)
        if not mini <= self.__screen_pos <= maxi:
            self.__screen_pos = mini if self.__screen_pos < mini else maxi
        self.screen.scroll(0, self.__screen_pos)
    
    def scroll_up(self, mini: int):
        self.__screen_pos -= self.scroll_movement
        if not mini <= self.__screen_pos:
            self.__screen_pos = mini
        self.screen.scroll(0, self.__screen_pos)
    
    def scroll_down(self, maxi: int):
        self.__screen_pos += self.scroll_movement
        if not self.__screen_pos <= maxi:
            self.__screen_pos = maxi
        self.screen.scroll(0, self.__screen_pos)

    @property
    def screen_pos(self) -> int:
        """the scrolling position of the screen"""
        return self.__screen_pos

    @screen_pos.setter
    def screen_pos(self, value: int) -> None:
        self.__screen_pos = value
        self.screen.scroll(0, self.__screen_pos)


if __name__ == "__main__":
    Screen()