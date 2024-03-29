import logging

import pygame

from constants import COLOURS, SCENE_MINESWEEPER
from settings import window_width, window_height
from scenes.scene import Scene
from objects.button import Button
from objects.game_object import GameObject


log = logging.getLogger(__name__)


class MainMenu(Scene):

    """A scene class to be used as a main menu."""

    def __init__(self):

        super().__init__()

        ## Create sprite groups
        self.create_group("text", pygame.sprite.LayeredDirty)
        self.create_group("buttons", pygame.sprite.LayeredDirty)
        self.create_group("draw", pygame.sprite.LayeredDirty)

        self._setup_scene()

        log.info("Main menu scene initialised")
    
    def _setup_scene(self) -> None:

        ## Load assets
        # Title
        title_image = pygame.font.SysFont("", 120).render(
            "Minesweeper", True, COLOURS["White"]
        )

        # Start button
        start_button_image = pygame.Surface((150, 50))
        start_button_image.fill(COLOURS["Grey"])
        start_button_image_text = pygame.font.SysFont("", 40).render(
            "Start", True, COLOURS["White"]
        )
        start_button_image.blit(
            start_button_image_text,
            (
                start_button_image.get_width() // 2
                - start_button_image_text.get_width() // 2,
                start_button_image.get_height() // 2
                - start_button_image_text.get_height() // 2,
            ),
        )

        # Quit button
        quit_button_image = pygame.Surface((150, 50))
        quit_button_image.fill(COLOURS["Grey"])
        quit_button_image_text = pygame.font.SysFont("", 40).render(
            "Quit", True, COLOURS["White"]
        )
        quit_button_image.blit(
            quit_button_image_text,
            (
                quit_button_image.get_width() // 2
                - quit_button_image_text.get_width() // 2,
                quit_button_image.get_height() // 2
                - quit_button_image_text.get_height() // 2,
            ),
        )

        ## Create objects
        # Title
        title = GameObject(
            window_width // 2 - title_image.get_width() // 2,
            int((window_height - title_image.get_height() // 2) * 0.1),
            title_image,
            self.sprite_groups["text"],
        )

        def start_button_function() -> None:
            log.info("Start button pressed")
            pygame.event.post(pygame.event.Event(SCENE_MINESWEEPER))

        # Start button
        start_button = Button(
            window_width // 2 - start_button_image.get_width() // 2,
            int((window_height - start_button_image.get_height() // 2) * 0.40),
            start_button_image,
            self.sprite_groups["buttons"],
            function=start_button_function,
        )

        # Quit button
        def quit_button_function() -> None:
            log.info("Quit button pressed")
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        quit_button = Button(
            window_width // 2 - quit_button_image.get_width() // 2,
            int((window_height - quit_button_image.get_height() // 2) * 0.50),
            quit_button_image,
            self.sprite_groups["buttons"],
            function=quit_button_function,
        )

        background = pygame.Surface((window_width, window_height)).convert()
        background.fill(COLOURS["Dark Grey"])
        self.sprite_groups["draw"].clear(background, bgd=background)

        self.sprite_groups["draw"].add(self.sprite_groups["text"], layer=1)
        self.sprite_groups["draw"].add(self.sprite_groups["buttons"], layer=2)

    def update(self, event_list: list) -> None:

        """Method to manage scene behaviour.

        Parameters
        ----------
        event_list : list
            An event list that is passed down for event handling."""

        for event in event_list:

            match event.type:

                case pygame.MOUSEBUTTONDOWN if event.button == pygame.BUTTON_LEFT:

                    pos = pygame.mouse.get_pos()

                    clicked_buttons = [
                        btn
                        for btn in self.sprite_groups["buttons"]
                        if btn.rect.collidepoint(pos)
                    ]

                    log.debug(f"Clicked at {pos[0], pos[1]}")

                    for button in clicked_buttons:
                        button.function()
    
    def draw(self, window: pygame.surface.Surface) -> None:

        """Method to render the scene.

        This implementation is blank, designed to act as a hook to be overwritten in extended scenes.

        Parameters
        -------
        window : pygame.surface.Surface
            The window surface to be drawn on.
        """

        self.sprite_groups["draw"].draw(window)
