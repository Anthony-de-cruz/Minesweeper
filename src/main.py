import logging as log

import pygame

from game import Game
import logger


def main() -> None:

    logger.setup_logging()

    pygame.init()

    log.info("Starting")

    game = Game()
    game.mainloop()

    log.info("Quitting")
    pygame.quit()
    raise SystemExit


if __name__ == "__main__":

    main()
