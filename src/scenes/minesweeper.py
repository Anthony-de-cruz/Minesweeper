import logging

import pygame

import settings
from constants import COLOURS
from scenes.scene import Scene
from sprite_camera import SpriteCamera
from objects.game_object import GameObject
from objects.minefield import Minefield


log = logging.getLogger(__name__)


class Minesweeper(Scene):

    """A scene class to be used as the main game."""

    def __init__(self, *group: pygame.sprite.Group) -> None:

        super().__init__(*group)

        self.create_group("draw", pygame.sprite.LayeredDirty)
        self.create_group("ui", pygame.sprite.Group)
        self.create_group("camera_0", SpriteCamera)
        self.create_group("clickable", pygame.sprite.Group)
        self.create_group("minefield", pygame.sprite.Group)

        ui = GameObject(
            300,
            100,
            pygame.surface.Surface((100, 100)),
            self.sprite_groups["ui"],
        )

        ui.image.fill((COLOURS["Grey"]))

        Minefield(
            0,
            0,
            20,
            20,
            self.sprite_groups["minefield"],
            self.sprite_groups["camera_0"],
        )

    def update(self, event_list: list) -> None:

        """Method to manage scene behaviour.

        Parameters
        ----------
        event_list : list
            An event list that is passed down for event handling."""

        # Too many indents
        for event in event_list:

            match event.type:

                case pygame.MOUSEBUTTONDOWN if event.button == pygame.BUTTON_LEFT:

                    click_pos = pygame.mouse.get_pos()

                    for sprite in self.sprite_groups["clickable"]:
                        if sprite.rect.collidepoint(click_pos):

                            if isinstance(sprite, Minefield) and event.button == pygame.BUTTON_LEFT:
                                sprite.uncover(click_pos)

        self._handle_inputs()

        self.sprite_groups["ui"].update()
        self.sprite_groups["minefield"].update()

    def _handle_inputs(self) -> None:

        """Method to handle inputs."""

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

            self.sprite_groups["camera_0"].move(
                (keys[pygame.K_a] - keys[pygame.K_d]) * settings.camera_speed,
                (keys[pygame.K_w] - keys[pygame.K_s]) * settings.camera_speed,
            )

    def draw(self, window: pygame.surface.Surface):

        """Method to draw the scene.

        Parameters
        -------
        window : pygame.surface.Surface
            The window surface to be drawn on.
        """

        self.image.fill(COLOURS["Dark Grey"])

        self.sprite_groups["minefield"].draw(self.image)
        self.sprite_groups["ui"].draw(self.image)

        
