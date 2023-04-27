# -*- coding: utf-8 -*-

from GUI.initialisation import *
from GUI.color import Color
from GUI.interact_object import Interact_Object

class Sub_Menu:
    
    def __init__(self, height, wigth, objects: list, backgroude_color, title=None, title_font=None, title_size=None, title_color=None, border_radius=30) -> None:
        self.__size = resize(height), resize(wigth)
        self.__background_color = Color(*backgroude_color)
        self.__border_radius = border_radius
        self.__background = self.__init_background()

        self.__init_title(title, title_font, title_size, title_color)

        self.__objects = objects

        self.scroll_movement = resize(50)
        self.__scroll_pos = 0

    def __init_title(self, title: str, title_font: str, title_size: int, title_color: tuple):
        self.__title = title
        if title:
            self.__title_size = resize(title_size)
            self.__title_font = pygame.sysfont.SysFont(title_font, self.__title_size)
            self.__title_color = Color(*title_color)
            self.__title_surface = self.__title_font.render(self.__title, True, self.__title_color)

    def __init_background(self):
        surface = pygame.Surface(self.__size).convert_alpha()
        surface.fill((0,0,0,0))
        pygame.draw.rect(surface, self.__background_color, (0, 0, *self.__size), border_radius=self.__border_radius)
        surface = pygame.transform.rotate(surface, self.__angle)
        surface.blit(self.__title_surface)
        return surface

    def __get_title_pos(self, pos):
        pass

    def __change_background(self):
        self.__background.fill((0,0,0,0))
        pygame.draw.rect(self.__background, self.__background_color, (0, 0, *self.__size), border_radius=self.__border_radius)


    def add_objects(self, objects):
        self.__objects += list(objects)

    def remove_objects(self, objects):
        if isinstance(objects, Interact_Object):
            self.__objects.remove(objects)
        if isinstance(objects, tuple) or isinstance(objects, list):
            for elt in objects:
                self.__objects.remove(elt)
    
    def update(self, *args, **kwargs):
        for elt in self.__objects:
            elt.update(*args, **kwargs)
    
    def draw(self, surface):
        for elt in self.__objects:
            elt.draw()


    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, value: str):
        if self.__title and value:
            self.__title = value
            self.__title_surface = self.__title_font.render(self.__title, True, self.__title_color)
            return
        raise ValueError("Can not assigne a title")

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        self.__size = value
        self.__background = self.__init_background()
    
    @property
    def border_radius(self):
        return self.__border_radius
    @border_radius.setter
    def border_radius(self, value):
        self.__border_radius = value
        self.__change_background()
    
    @property
    def background_color(self):
        return self.__background_color
    @background_color.setter
    def background_color(self, value):
        self.__background_color = Color(*value)
        self.__change_background()

    @property
    def screen_pos(self) -> int:
        """the scrolling position of the menu"""
        return self.__scroll_pos
    @screen_pos.setter
    def screen_pos(self, value: int) -> None:
        self.__scroll_pos = value
        self.__background.scroll(0, self.__scroll_pos)
