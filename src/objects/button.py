from types import FunctionType
import logging as log

import pygame

from objects.game_object import GameObject


def unassigned_function() -> None:

    """A method to represent the function of a button when pressed.
    Overwritten when a function is passed."""

    log.warning("Button function unassigned")


class Button(GameObject):

    """A button object that contains a function."""

    def __init__(
        self,
        x_coord: int,
        y_coord: int,
        image: pygame.Surface,
        *group: pygame.sprite.Group,
        function=unassigned_function
    ):

        super().__init__(x_coord, y_coord, image, *group)

        self.function = function
