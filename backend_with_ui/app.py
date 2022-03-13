import json

from flask import Flask, render_template, request
from requests import post

app = Flask(__name__)


@app.route("/", methods=['get'])
def index():
    render_template('index.html')


@app.route("/map/", methods=['post', 'get'])
def mapview_frac():
    # creating a map in the view
    if request.method == 'POST':
        with open('backend_with_ui/static/fractions.json', 'r') as file:
            data = json.load(file)
        id = data.get(request.form.get('frac'))
        res = post('http://142.93.129.164:8080/id', data={'id': id})
        res_api = res.json()
        coords = res_api['trashers']
        return render_template('map.html', coords=coords)
    else:
        return render_template('map.html')


@app.route("/mapn/", methods=['post', 'get'])
def mapview_mark():
    # creating a map in the view
    if request.method == 'POST':
        form = True
        with open('backend_with_ui/static/marking_id.json', 'r') as file:
            data = json.load(file)
        if data.get(request.form.get('mark').upper()):
            id = int(data.get(request.form.get('mark').upper()))
        else:
            err = 'Такой вид отходов не перерабатывается в Краснодаре'
            return render_template('mapn.html', form=False, err=err)
        res = post('http://142.93.129.164:8080/id', data={'id': str(id)})
        res_api = res.json()
        coords = res_api['trashers']
        return render_template('mapn.html', coords=coords, form=form)
    else:
        return render_template('mapn.html')


if __name__ == '__main__':
    app.run(debug=True)
