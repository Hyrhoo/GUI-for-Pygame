# -*- coding: utf-8 -*-

from GUI.screen import Screen
from GUI.interact_object import Interact_Object
from GUI.__init import *

class Menu:
    def __init__(self, screen: Screen, sub_menus: list[Interact_Object]) -> None:
        self.screen = screen
        self.sub_menus = sub_menus
