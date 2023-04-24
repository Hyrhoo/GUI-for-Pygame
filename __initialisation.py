# -*- coding: utf-8 -*-
import sys
import os
import pathlib
import pygame
from typing import overload

pygame.mixer.pre_init()
pygame.init()
pygame.mixer.set_num_channels(32)
