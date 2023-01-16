from logging import log

import pygame

from settings import window_width, window_height


class Scene(pygame.sprite.Sprite):

    """A primitive scene type. To be used to extend new scenes that overwrite it's methods."""

    def __init__(self, *group: pygame.sprite.Group):

        super().__init__(*group)

        ## Create surface
        self.image = pygame.display.get_surface()
        self.rect = self.image.get_rect()

        self.width = self.rect.size[0]
        self.height = self.rect.size[1]

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
