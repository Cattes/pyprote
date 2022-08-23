"""Entry point to the cli commands."""
import argparse
import logging
from logging.config import dictConfig

from pyprote.logging_config.logger_config import get_logger_config
from pyprote.pyprote import funone

dictConfig(get_logger_config())


def main():
    """Main example."""
    logging.info("Running pyprote on the command line: ")
    funone_res = funone(1)
    logging.info(f"This is f1(): {funone_res}")


if __name__ == "__main__":
    # add argparse to the main function to handle cli input
    parser = argparse.ArgumentParser(description="Pyprote")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
    args = parser.parse_args()

    main()
