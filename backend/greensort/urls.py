from aiohttp import web
from .views import get_by_id

urls = [
    web.post('/', get_by_id),
]
