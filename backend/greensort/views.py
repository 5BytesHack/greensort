from aiohttp import web
import json


async def get_by_id(request):
    id = request.query.get('id')
    with open('/static/data.json', 'r') as data_file:
        data = json.load(data_file)
    trashers = []
    for key in data.keys():
        if id in data[key]['types']:
            trashers.append(data[key]['coords'])
    return web.Response(text=' '.join(trashers))
