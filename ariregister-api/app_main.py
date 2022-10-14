from unicodedata import name
import flask
from flask import request, jsonify
from flask_cors import CORS
import app_db

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config["DEBUG"] = True
app.config["DATABASE"] = 'database.db'

@app.route('/', methods=['GET'])
def home():
    res = {'OK': 'API service for Äriregister project'}
    return jsonify(res)

@app.route('/api/v1/company', methods=['GET'])
def get_company():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        res = {'ERROR': 'No id field provided'}
        return jsonify(res)
    results = app_db.getCompanyBasicData(app.config["DATABASE"], id)
    return jsonify(results)

@app.route('/api/v1/searchCompany', methods=['GET'])
def search_company():
    if 'searchstring' in request.args:
        str = request.args['searchstring']
        if len(str) < 4:
            res = {'ERROR': 'Searchstring should be at least 4 symbols long'}
            return jsonify(res)
    else:
        res = {'ERROR': 'No searchstring field provided'}
        return jsonify(res)
    results = app_db.getSearchedCompanies(app.config["DATABASE"], str)
    return jsonify(results)

@app.route('/api/v1/companyOwners', methods=['GET'])
def get_owners():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        res = {'ERROR': 'No id field provided'}
        return jsonify(res)
    results = app_db.getCompanyOwners(app.config["DATABASE"], id)
    return jsonify(results)

@app.route('/api/v1/list/<list_name>', methods=['GET'])
def get_list(list_name):
    print(list_name)
    results = app_db.getList(app.config["DATABASE"], list_name)
    return jsonify(results)
    
app.run()