import pygame


class GameObject(pygame.sprite.Sprite):

    """A generic game object that is created with x/y coordinates and an image.
    The constructor generates width/height values and a Rect object."""

    def __init__(
        self,
        x_coord: int,
        y_coord: int,
        image: pygame.surface.Surface,
        *group: pygame.sprite.Group
    ):

        super().__init__(*group)

        self.image = image

        # Create dimentions
        self.width = image.get_width()
        self.height = image.get_height()

        self.rect = pygame.Rect(x_coord, y_coord, self.width, self.height)
