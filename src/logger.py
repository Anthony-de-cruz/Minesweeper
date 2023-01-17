import logging
import logging.config


def setup_logging(
    name: str,
    level: int,
    message_format: str = "%(asctime)s|%(levelname)s|%(name)s| %(message)s",
    date_format: str = "%H:%M:%S",
) -> logging.Logger:

    """Setup a logger.

    Parameters
    ----------
        name: str
            A name for the logger, such as the Module __name__.

        level: int
            Logging level. Refer to logging.DEBUG - logging.CRITICAL.

        message_format: str
            The log message format.

        date_format: str
            The date format, assuming that it is even used.

    Returns
    -------
        logger: logging.Logger
            The created logger."""

    logging.basicConfig(level=level, format=message_format, datefmt=date_format)

    logger = logging.getLogger(name)

    # Colours!
    logging.addLevelName(
        logging.WARNING, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.WARNING)
    )
    logging.addLevelName(
        logging.ERROR, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.ERROR)
    )
    logging.addLevelName(
        logging.CRITICAL,
        "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.CRITICAL),
    )

    return logger
