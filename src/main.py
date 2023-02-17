import logging

import pygame

import logger
from game import Game


def main() -> None:

    log = logger.setup_logging(__name__, logging.DEBUG)

    pygame.init()

    log.info("Starting")

    game = Game()
    game.mainloop()

    log.info("Quitting")
    pygame.quit()
    raise SystemExit


if __name__ == "__main__":

    main()
