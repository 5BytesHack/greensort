from aiohttp import web
from .views import get_by_id

urls = [
    web.post('/', get_by_id),
    web.static('/prefix', 'backend', follow_symlinks=True, show_index=True)
]
