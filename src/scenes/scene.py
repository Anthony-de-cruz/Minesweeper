from logging import log

import pygame

from settings import window_width, window_height


class Scene(pygame.sprite.Sprite):

    """A primitive scene type; subclass of pygame.sprite.Sprite

    Scenes are objects that contain game "scenes", such as levels.
    Scenes handle the logic of the objects within them.

    To be used to extend new scenes that overwrite it's methods.

    Scene attributes
    ----------------
        image: pygame.surface.Surface
            The scene surface; inherited from pygame.sprite.Sprite

        rect: pygame.rect.Rect
            The scene's rect; inherited from pygame.sprite.Sprite

        width: int
            The scene's width dimention.

        height: int
            The scene's height dimention.

        sprite_groups: dict[pygame.sprite.AbstractGroup]
            A dictionary intended to keep all of a scenes sprite groups.

            Can be used to update all sprites, ect. Usage is optional."""

    def __init__(self, *group: pygame.sprite.Group) -> None:

        super().__init__(*group)

        ## Create surface
        self.image = pygame.display.get_surface()
        self.rect = self.image.get_rect()

        self.width = self.rect.size[0]
        self.height = self.rect.size[1]

        self.sprite_groups = {}

    def create_group(self, name: str, group_type: type[pygame.sprite.AbstractGroup]):

        """Method to create a sprite group and add it to self.sprite_groups.

        Parameters
        ----------
            name: str
                The name of the sprite group. Used as a key for access.

            group_type: type[pygame.sprite.AbstractGroup]
                The type of sprite group you want it to be."""

        self.sprite_groups[name] = group_type()

    def update(self, event_list: list) -> None:

        """Method to manage scene behaviour.

        This implementation is blank, designed to act as a hook to be overwritten in extended scenes.

        Parameters
        ----------
        event_list : list
            An event list that is passed down for event handling."""

    def render(self) -> pygame.surface.Surface:

        """Method to render the scene.

        This implementation is blank, designed to act as a hook to be overwritten in extended scenes.

        Returns
        -------
        self.image : pygame.surface.Surface
            The rendered image.
        """

        return self.image
