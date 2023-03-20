import os
import logging

import pygame

from settings import window_width, window_height, window_name, fps
import constants
from scene_handler import SceneHandler
from scenes import main_menu, minesweeper


log = logging.getLogger(__name__)


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

        ## Initial State
        self.running = True
        pygame.event.post(pygame.event.Event(constants.SCENE_MAIN_MENU))
        log.info("Game initialised")

    def setup_window(self) -> pygame.surface.Surface:

        """Generates and returns a window surface.

        Returns
        -------
            pygame.Surface: The generated window surface."""

        window = pygame.display.set_mode(
            (self.window_width, self.window_height))
        pygame.display.set_caption((self.window_name))
        os.environ["SDL_VIDEO_CENTERED"] = "1"

        return window

    def handle_events(self) -> list:

        """Fetches the event list, processes it and returns it.

        May be changed into it's own event handler class in the future.

        Returns
        -------
            list: The event list."""

        event_list = pygame.event.get()

        for event in event_list:

            match event.type:

                case pygame.QUIT:

                    self.running = False

                case constants.SCENE_MAIN_MENU:

                    log.info("Setting scene to: Main menu")
                    self.scene_handler.create_scene("main_menu", main_menu.MainMenu())
                    self.scene_handler.set_focus("main_menu")

                case constants.SCENE_MINESWEEPER:

                    log.info("Setting scene to: Minesweeper")
                    self.scene_handler.create_scene(
                        "minesweeper", minesweeper.Minesweeper()
                    )
                    self.scene_handler.set_focus("minesweeper")

        return event_list

    def mainloop(self) -> None:

        """Main program loop."""

        while self.running:

            self.clock.tick(self.fps)
            event_list = self.handle_events()

            self.scene_handler.update_focus(event_list)
            self.scene_handler.draw_focus(self.window)

            pygame.display.flip()
