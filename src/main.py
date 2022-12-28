import os
import logging as log

import pygame

def main():

    log.basicConfig(
        format = "%(asctime)s|%(levelname)s|%(name)s| %(message)s",
        datefmt = "%H:%M:%S",
        level = os.environ.get("LOGLEVEL", "DEBUG"),
    )

    pygame.init()

    log.info("Starting game")
    

if __name__ == "__main__":

    main()
