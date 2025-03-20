import logging

def setup_logging():
    """Configure logging for the application."""
    logging.basicConfig(
        filename='lockpy.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )