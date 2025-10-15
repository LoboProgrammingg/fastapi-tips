import logging

def configure_logging():
    """Configura o logger principal da aplicação com um formato consistente."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger("mini-crm-fastapi")

logger = configure_logging()