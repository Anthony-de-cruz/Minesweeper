import logging as log

import pygame

from constants import COLOURS
from scenes.scene import Scene


class ParticleTest(Scene):

    """A scene to be used to demonstrate the particle system."""

    def __init__(self, *group: pygame.sprite.Group):

        super().__init__(*group)

        self.sprite_groups = {}

        self.sprite_groups["particles"] = pygame.sprite.Group()

    def update(self, event_list: list) -> None:

        """Method to manage scene behaviour.

        Parameters
        ----------
        event_list : list
            An event list that is passed down for event handling."""

        for event in event_list:

            if event == pygame.BUTTON_LEFT:

                log.debug("WEEEE")

    def render(self) -> pygame.surface.Surface:

        """Method to render the scene.

        Returns
        -------
        self.image : pygame.surface.Surface
            The rendered image.
        """

        self.image.fill(COLOURS["Dark Grey"])

        return self.image
