# -*- coding: utf-8 -*-

import sys
import os
import pathlib
import pygame
from multipledispatch import dispatch

pygame.mixer.pre_init()
pygame.init()
pygame.mixer.set_num_channels(32)

DEFAULT_SCREEN_SIZE = (1920, 1080)
SCREEN_INFO = pygame.display.Info()
SCREEN_SIZE = SCREEN_INFO.current_w, SCREEN_INFO.current_h # (650, 500) (1536, 864)
multi_reso = min(SCREEN_SIZE[0] // DEFAULT_SCREEN_SIZE[0], SCREEN_SIZE[1] // DEFAULT_SCREEN_SIZE[1])

def resize(values: int | float) -> float:
    """Useful function to resize a value to fit the user's screen size.

    Args:
        - values (int | float): The value to resize.

    Returns:
        - float: The resized value.
    """
    return values * multi_reso