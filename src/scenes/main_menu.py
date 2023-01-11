import pygame

import logging as log
from scenes.scene import Scene
from constants import COLOURS

class MainMenu(Scene):

    """A scene object to be used as a main menu."""

    def __init__(self, *group: pygame.sprite.Group):

        super().__init__(group)

        ## Create sprite groups
        self.sprite_groups = {}

        self.sprite_groups["text"] = pygame.sprite.Group()
        self.sprite_groups["buttons"] = pygame.sprite.Group()

        log.info("Main menu scene initialised")

    def update(self, event_list: list) -> None:

        """Method to manage scene behaviour.

        Parameters
        ----------
        event_list : list
            An event list that is passed down for event handling."""

    
    def render(self) -> pygame.Surface:

        """Method to render the scene.

        Returns
        -------
        self.image : pygame.surface.Surface
            The rendered image.
        """

        self.image.fill(COLOURS["Grey"])

        self.sprite_groups["text"].draw(self.image)
        self.sprite_groups["buttons"].draw(self.image)

        return self.image
