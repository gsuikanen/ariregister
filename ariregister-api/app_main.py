from unicodedata import name
import flask
from flask import request, jsonify
from flask_cors import CORS
import app_db
from validators import validateCompanyData, validateOwners

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

@app.route('/api/v1/company', methods=['POST'])
def add_company():
    data =  request.get_json()
    print(data)
    #Validating data
    validation_res = validateCompanyData(data)
    if validation_res != '':
        res = {'ERROR': validation_res}
        return jsonify(res)
    if app_db.getCompanyMatches(app.config["DATABASE"], data['companyCode'], data['companyName']):
        res = {'ERROR': 'Duplicating company\nCheck that company name and registration code are unique'}
        return jsonify(res)
    owners = data['owners']
    validation_res = validateOwners(owners)
    if len(validation_res) > 0:
        return jsonify(validation_res)
    #Saving data to DB
    company_id = app_db.addCompany(app.config["DATABASE"], data['companyName'], data['companyCode'], data['companyRegdt'])
    for own in owners:
        if own['ownerType'] == 'bus':
            own['ownerSurname'] = ''
        app_db.addCompanyOwner(app.config["DATABASE"], company_id, own['ownerName'], own['ownerSurname'], own['ownerType'], own['ownerCode'], 'found', own['ownerCapital'])
    res = {'company_id': company_id}
    return jsonify(res)

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