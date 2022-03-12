from aiohttp import web

from greensort.urls import urls


app = web.Application()
app.add_routes(urls)
web.run_app(app)

# import json
# import pymongo

# client = pymongo.MongoClient(host='localhost', port=27017)
# db = client.db
# collection = db.trashers
# r = []
#
# with open('static/data.json', 'r') as data_file:
#     for data in data_file:
#         d = json.loads(data)
#         r.append(pymongo.InsertOne(d))
#
# res = collection.bulk_write(r)
# client.close()



