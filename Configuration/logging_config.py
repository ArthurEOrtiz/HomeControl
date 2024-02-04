
import logging

def configure_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("application.log"),
            logging.StreamHandler()
        ]
    )

def log_attributes(logger, attributes):
    for attribute, value in attributes.items():
        logger.info(f"{attribute.capitalize()}: {value}")