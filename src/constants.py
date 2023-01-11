from dataclasses import dataclass

import pygame

@dataclass
class SceneChangeEvents:

    main_menu: pygame.event.Event

COLOURS = {"Black": (0, 0, 0), "White": (255, 255, 255), "Grey": (100, 100, 100)}
