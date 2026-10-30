from logtail import LogtailHandler
import logging
from settings import settings

handler = LogtailHandler(
    source_token=settings.BS_TOKEN,
    host=f'https://{settings.BS_HOST}',
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.handlers = []
logger.addHandler(handler)
