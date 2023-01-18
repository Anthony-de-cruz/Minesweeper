from dataclasses import dataclass
from typing import Tuple

import pygame

from objects.game_object import GameObject


@dataclass
class Tile:

    mined: bool
    number: int
    covered: bool = True

    def uncover(self):
        self.covered = False


class Minefield(GameObject):

    """A class to represent the minefield."""

    def __init__(
        self,
        x_coord: int,
        y_coord: int,
        rows: int,
        columns: int,
        *group: pygame.sprite.Group,
    ):

        # Get from somewhere eventually
        self.tile_width, self.tile_height = 40, 40

        super().__init__(
            x_coord,
            y_coord,
            pygame.surface.Surface(
                (self.tile_width * rows, self.tile_height * columns)
            ),
            *group,
        )

        self.minefield = {}

        for row in range(rows):
            for column in range(columns):

                self.minefield[(row, column)] = Tile(False, 0)

    def uncover(self, click_pos: Tuple[int, int]) -> None:

        """Method to act as a common way to interact.

        Parameters
        ----------
            click_pos : Tuple[int, int]
                A tuple containing x and y coordinates."""

        self.minefield[(click_pos[0] // self.tile_width, click_pos[0] // self.tile_height)].uncover()


    def update(self):

        pass
