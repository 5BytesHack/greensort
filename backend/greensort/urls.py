from aiohttp import web
from .views import get_by_id, get_by_id_and_location

urls = [
    web.post('/id', get_by_id),
    web.post('/location', get_by_id_and_location)
]
