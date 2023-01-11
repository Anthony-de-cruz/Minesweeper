import logging as log

import pygame

from scenes.scene import Scene
from constants import COLOURS
from objects.button import Button
from objects.game_object import GameObject


class MainMenu(Scene):

    """A scene object to be used as a main menu."""

    def __init__(self, *group: pygame.sprite.Group):

        super().__init__(group)

        ## Create sprite groups
        self.sprite_groups = {}

        self.sprite_groups["text"] = pygame.sprite.Group()
        self.sprite_groups["buttons"] = pygame.sprite.Group()

        ## Load assets
        title_image = pygame.font.SysFont(None, 120).render(
            "Minesweeper", True, COLOURS["White"]
        )

        start_button_image = pygame.Surface((150, 50))
        start_button_image.fill(COLOURS["Grey"])
        start_button_image_text = pygame.font.SysFont(None, 40).render(
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

        quit_button_image = pygame.Surface((150, 50))
        quit_button_image.fill(COLOURS["Grey"])
        quit_button_image_text = pygame.font.SysFont(None, 40).render(
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
        title = GameObject(
            self.width // 2 - title_image.get_width() // 2,
            int((self.height - title_image.get_height() // 2) * 0.1),
            title_image,
            self.sprite_groups["text"],
        )

        start_button = Button(
            self.width // 2 - start_button_image.get_width() // 2,
            int((self.height - start_button_image.get_height() // 2) * 0.40),
            start_button_image,
            self.sprite_groups["buttons"],
        )

        def quit_button_function() -> None:
            log.info("Quit button pressed")
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        quit_button = Button(
            self.width // 2 - quit_button_image.get_width() // 2,
            int((self.height - quit_button_image.get_height() // 2) * 0.50),
            quit_button_image,
            self.sprite_groups["buttons"],
            function=quit_button_function,
        )

        log.info("Main menu scene initialised")

    def update(self, event_list: list) -> None:

        """Method to manage scene behaviour.

        Parameters
        ----------
        event_list : list
            An event list that is passed down for event handling."""

        for event in event_list:

            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == pygame.BUTTON_LEFT
            ):
                pos = pygame.mouse.get_pos()

                clicked_buttons = [
                    btn
                    for btn in self.sprite_groups["buttons"]
                    if btn.rect.collidepoint(pos)
                ]

                log.debug(f"Clicked at {pos[0], pos[1]}")

                for button in clicked_buttons:
                    button.function()

    def render(self) -> pygame.Surface:

        """Method to render the scene.

        Returns
        -------
        self.image : pygame.surface.Surface
            The rendered image.
        """

        self.image.fill(COLOURS["Dark Grey"])

        self.sprite_groups["text"].draw(self.image)
        self.sprite_groups["buttons"].draw(self.image)

        return self.image
