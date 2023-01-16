from typing import List

import pygame


class SpriteCamera(pygame.sprite.Group):

    """A camera class; subclass of pygame.sprite.Group.

    Applies camera movement to all contained sprites to simulate a controllable
    camera by applying a camera offset vector to the rect of all contained
    sprites.

    Not intended to be used to draw/update the contained sprites.

    Stores an offset vector to record camera movements."""

    def __init__(self, *sprites: pygame.sprite.Sprite) -> None:

        super().__init__(*sprites)

        self._offset_vector = [0, 0]

    def move(self, x: int, y: int) -> None:

        """Move the camera offset by the passed amount.

        Parameters
        ----------
            x: int
                Modification to the X axis.

            y: int
                Modification to the Y axis."""

        self._offset_vector[0] += x
        self._offset_vector[1] += y

        for sprite in self.sprites():

            sprite.rect.x += x
            sprite.rect.y += y

    def set_offset(self, x: int, y: int) -> None:

        """Set the camera offset to the passed amount.

        Parameters
        ----------
            x: int
                Set the X axis.

            y: int
                Set the Y axis."""

        old_offset = self._offset_vector

        self._offset_vector[0], self._offset_vector[1] = x, y

        for sprite in self.sprites():

            sprite.rect.x -= old_offset[0]
            sprite.rect.y -= old_offset[1]

            sprite.rect.x += self._offset_vector[0]
            sprite.rect.y += self._offset_vector[1]

            if hasattr(sprite, "dirty"):
                if sprite.dirty == 0:
                    sprite.dirty = 1
