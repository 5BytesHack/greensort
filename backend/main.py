from aiohttp import web
import pathlib

from greensort.urls import urls


app = web.Application()
app.add_routes(urls)
web.run_app(app)
