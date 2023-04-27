# -*- coding: utf-8 -*-

from GUI.screen import Screen
from GUI.color import Color
from GUI.initialisation import *

class Interact_Object:
    OBJECT_RADIUS = 9999999
    DARCKER_POURCENTAGE = 20

    def __init__(self, screen: Screen, x: float, y: float, width: float, height: float, object_color: tuple[int, int, int], border_color: tuple[int, int, int], fixe: bool = True) -> None:
        """initialise an interact object. all the values are absolut valiues

        Args:
            screen (Screen): the surface to blits on
            x (float): absolut value x of the center of the object
            y (float): absolut value y of the center of the object
            width (float): absolut value of the width of the object
            height (float): absolut value of the height of the object
            object_color (tuple[int, int, int]): the color of the object
            border_color (tuple[int, int, int]): the color of the border of the object
            fixe (bool) default is True: if the object is fixe or not
        """
        self.screen = screen
        self.x = self.screen.resize(x)
        self.y = self.screen.resize(y)
        self.width = self.screen.resize(width)
        self.height = self.screen.resize(height)
        self.object_color = Color(*object_color)
        self.border_color = Color(*border_color)
        self.border_radius = min(self.height, self.width) // 8
        self.fixe = fixe

        self.surfaces = self.__creat_surfaces()
        self.image = self.surfaces[0]
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
        self.is_select = False
        self.is_over = False
        self.is_cliqued = False
        self.is_sound_played = False

    def __creat_surfaces(self):
        surf1 = pygame.Surface((self.width, self.height)).convert_alpha()
        surf1.fill((0, 0, 0, 0))
        surf2 = pygame.Surface((self.width, self.height)).convert_alpha()
        surf2.fill((0, 0, 0, 0))
        rect = pygame.Rect(0, 0, self.width, self.height)
        rad1 = self.screen.resize(self.OBJECT_RADIUS)
        rad2 = self.screen.resize(self.border_radius)
        pygame.draw.rect(surf1, self.object_color, rect, border_radius=rad1)
        pygame.draw.rect(surf1, self.border_color, rect, rad2, rad1)
        pygame.draw.rect(surf2, self.object_color.copy().darken(self.DARCKER_POURCENTAGE), rect, border_radius=rad1)
        pygame.draw.rect(surf2, self.border_color.copy().darken(self.DARCKER_POURCENTAGE), rect, rad2, rad1)
        return surf1, surf2

    def updat(self, surface) -> None:
        self.is_sound_played_func()
        self.display(surface)
    
    def interact(self, event: pygame.event.Event):
        self.is_over_func(event)
        self.is_cliqued_func(event)
        

    def display(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rect)

    def is_select_func(self) -> None:
        pass

    def is_over_func(self, event: pygame.event.Event) -> None:
        """
        this fonction change the value of self.is_over:
            - to True is the cursor is over the object
            - to False otherways
        it must be call at every loop
        """
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            self.is_over = pygame.Rect.collidepoint(self.rect, x, y)

    def is_cliqued_func(self, event: pygame.event.Event) -> None:
        """
        the fonction change the value of self.is_cliqued:
            - to True if the mouse button is pressed over the object
            - to False if the mouse button is unpressed
        it must be call at every loop

        Args:
            event (pygame event): _description_
        """
        if self.is_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.is_cliqued = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.is_cliqued = False
        if not self.screen.screen.get_active():
            self.is_cliqued = False

    def is_sound_played_func(self) -> None:
        if not self.is_over and not self.is_cliqued:
            self.is_sound_played = False
        elif self.is_cliqued or self.is_over:
            self.is_sound_played = True

if __name__ == "__main__":
    screen = Screen()
    color1 = Color(255, 0, 255)
    color2 = color1.copy().darken(20)
    i_object = Interact_Object(screen, screen.mid_screen(screen.__DEFOLT_SCREEN_SIZE[0]), 
                               screen.mid_screen(screen.__DEFOLT_SCREEN_SIZE[1]),
                               200, 50, color1, color2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.screen.fill((0, 0, 0))
        i_object.display(screen.screen)
        pygame.display.flip()

