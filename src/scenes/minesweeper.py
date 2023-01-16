from logging import log

import pygame

import settings
from constants import COLOURS
from scenes.scene import Scene
from objects.game_object import GameObject


class Minesweeper(Scene):

    """A scene class to be used as the main game."""

    def __init__(self, *group: pygame.sprite.Group) -> None:

        super().__init__(*group)

        self.sprite_groups = {}

        self.sprite_groups["ui"] = pygame.sprite.Group()
        self.sprite_groups["camera_pan"] = pygame.sprite.Group()
        self.sprite_groups["field"] = pygame.sprite.Group()

        GameObject(
            300,
            100,
            pygame.surface.Surface((100, 100)),
            self.sprite_groups["camera_pan"],
            self.sprite_groups["ui"],
        )

    def update(self, event_list: list) -> None:

        """Method to manage scene behaviour.

        Parameters
        ----------
        event_list : list
            An event list that is passed down for event handling."""

        for event in event_list:

            match event.type:

                case _:

                    pass

        self.handle_inputs()

    def handle_inputs(self) -> None:

        keys = pygame.key.get_pressed()

        if (
            keys[pygame.K_w]
            or keys[pygame.K_a]
            or keys[pygame.K_s]
            or keys[pygame.K_d]
            or keys[pygame.K_UP]
            or keys[pygame.K_LEFT]
            or keys[pygame.K_DOWN]
            or keys[pygame.K_RIGHT]
        ):

            for sprite in self.sprite_groups["camera_pan"]:

                sprite.rect.x += (
                    keys[pygame.K_d] - keys[pygame.K_a]
                ) * settings.camera_speed

                sprite.rect.y += (
                    keys[pygame.K_s] - keys[pygame.K_w]
                ) * settings.camera_speed

    def render(self) -> pygame.surface.Surface:

        """Method to render the scene.

        Returns
        -------
        self.image : pygame.surface.Surface
            The rendered image.
        """

        self.image.fill(COLOURS["Dark Grey"])

        self.sprite_groups["ui"].draw(self.image)

        return self.image
