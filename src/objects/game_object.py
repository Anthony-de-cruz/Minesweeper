import pygame


class GameObject(pygame.sprite.DirtySprite):

    """A generic game object class; subclass of pygame.sprite.DirtySprite

    Created with x/y coordinates and an image.
    The initialiser generates width/height values and a Rect object."""

    def __init__(
        self,
        x_coord: int,
        y_coord: int,
        image: pygame.surface.Surface,
        *group: pygame.sprite.Group
    ):

        super().__init__(*group)

        self.image = image
        self.rect = pygame.Rect(x_coord, y_coord, image.get_width(), image.get_height())
