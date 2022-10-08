import flask
from flask import request, jsonify
import app_db

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["DATABASE"] = 'database.db'

print(app)

#Test data
companies = [
    {'id': 1,
     'name': 'MEES JA KOER OÜ',
     'code': '12117629',
     'reg_dt': '08.06.2011',
     'owners': [
        {'name': 'Andre',
         'surname': 'Esna',
         'type': 'priv',
         'code': '3800308****',
         'role': 'founder',
         'amount': 2500
        },
     ]},
     {'id': 2,
     'name': 'MEES JA KASS OÜ',
     'code': '14013242',
     'reg_dt': '14.03.2016',
     'owners': [
        {'name': 'Veiko',
         'surname': 'Vostrjakov',
         'type': 'priv',
         'code': '3750207****',
         'role': 'founder',
         'amount': 1500
        },
        {'name': 'Martin',
         'surname': 'Vostrjakov',
         'type': 'priv',
         'code': '3780207***',
         'role': 'owner',
         'amount': 1000
        },
     ]},
]

@app.route('/', methods=['GET'])
def home():
    return 'API service for Äriregister project'

@app.route('/api/v1/company/all', methods=['GET'])
def all_companies():
    return jsonify(companies)


@app.route('/api/v1/company', methods=['GET'])
def get_company():
    if 'id' in request.args:
        id = int(request.args['id'])
        results = []
    else:
        return "Error: No id field provided. Please specify an id."
    for comp in companies:
        if comp['id'] == id:
            results.append(comp)
    return jsonify(results)

@app.route('/api/v1/list/<list_name>', methods=['GET'])
def get_list(list_name):
    print(list_name)
    results = app_db.getList(app.config["DATABASE"], list_name)
    return jsonify(results)
    
app.run()