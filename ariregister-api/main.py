import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

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
    return '''<h1>API service for Äriregister project</h1>
<p>This is a boilerplate code for Flask API service</p>'''

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
    
app.run()