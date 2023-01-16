from typing import List
from typing_extensions import override

import pygame


class SpriteCamera(pygame.sprite.AbstractGroup):

    """A camera class. Stores an offset vector to apply to a scene when drawn."""

    def __init__(self) -> None:

        self.offset_vector = pygame.Vector2(0.0, 0.0)

    @override
    def __init__(self, x_offset: float, y_offset: float) -> None:

        self.offset_vector = pygame.Vector2(x_offset, y_offset)

    def draw(self, surface: pygame.surface.Surface()) -> List[pygame.Rect]:

        """All contained sprites are drawn to the surface with applied offset vector.
        
        A modified version of pygame.sprite.AbstractGroup.draw 
        that simply applies the camera offset vector.
        
        Returns
        -------
            List[pygame.Rect]: A list of lost dirty sprites."""

        # Code copied from pygame.sprite.AbstractGroup.draw
        sprites = self.sprites()
        if hasattr(surface, "blits"):
            
            self.spritedict.update(
                zip(
                    sprites,
                    surface.blits(
                        (
                            spr.image,
                            # Modified to apply offset vector
                            spr.rect.move(self.offset_vector.y,self.offset_vector.y),
                        )
                        for spr in sprites
                    ),
                )
            )
        else:
            for spr in sprites:
                self.spritedict[spr] = surface.blit(spr.image, spr.rect)
        self.lostsprites = []
        dirty = self.lostsprites

        return dirty
