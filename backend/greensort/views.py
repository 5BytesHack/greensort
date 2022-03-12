from aiohttp import web
from pymongo import MongoClient
import json


async def get_by_id(request):
    """Получает в форме POST запросом id типа мусора и возвращает json из всех подходящих мусорок"""
    id = request.query.get('id')
    client = MongoClient(host='localhost', port=27017)
    db = client.db
    collection = db.trashers
    data_cur = collection.find()
    trashers = []
    for key in data_cur:
        data = key
    data.pop('_id')
    for key in data.keys():
        if int(id) in data[key]['types']:
            trashers.append(data[key]['coords'])
    return web.json_response({'trashers': trashers})
