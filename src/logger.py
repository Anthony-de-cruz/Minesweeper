import os
import logging


def setup_logging():

    logging.basicConfig(
        format="%(asctime)s|%(levelname)s|%(name)s| %(message)s",
        datefmt="%H:%M:%S",
        level=os.environ.get("LOGLEVEL", "DEBUG"),
    )

    logging.addLevelName(
        logging.WARNING, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.WARNING)
    )
    logging.addLevelName(
        logging.ERROR, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.ERROR)
    )
