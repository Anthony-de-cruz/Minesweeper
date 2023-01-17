from dataclasses import dataclass

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

                self.minefield[f"{row},{column}"] = Tile(False, 0)

        def uncover(self, click_pos):
            pass

        def update(self):

            pass
