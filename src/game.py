import os
import logging as log

import pygame

from settings import window_width, window_height, window_name, fps
from scene_handler import SceneHandler
from scenes import main_menu


class Game:

    """Main game class."""

    def __init__(self):

        ## Setup window
        self.window_width = window_width
        self.window_height = window_height
        self.window_name = window_name

        self.window = self.setup_window()

        ## Clock
        self.clock = pygame.time.Clock()
        self.fps = fps

        ## Scenes
        self.scene_handler = SceneHandler()
        self.scene_handler.create_scene("main_menu", main_menu.MainMenu())

        ## Initial State
        self.running = True
        self.scene_handler.set_focus("main_menu")
        log.info("Game initialised")

    def setup_window(self) -> pygame.Surface:

        """Generates and returns a window surface.

        Returns
        -------
            pygame.Surface: The generated window surface."""

        window = pygame.display.set_mode(
            (self.window_width, self.window_height)
        ).convert_alpha()
        pygame.display.set_caption((self.window_name))
        os.environ["SDL_VIDEO_CENTERED"] = "1"

        return window

    def handle_events(self) -> list:

        """Fetches the event list, processes it and returns it.

        Returns
        -------
            list: The event list."""

        event_list = pygame.event.get()

        for event in event_list:

            if event.type is pygame.QUIT:
                self.running = False

        return event_list

    def mainloop(self) -> None:

        """Main program loop."""

        while self.running:

            self.clock.tick(self.fps)
            event_list = self.handle_events()

            self.scene_handler.update_focus(event_list)

            self.window.blit(
                self.scene_handler.render_focus(),
                (0, 0),
                self.scene_handler.get_focus().rect,
            )

            pygame.display.flip()
