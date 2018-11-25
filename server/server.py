from flask import jsonify    
from flask import Flask

from engien.config import client

app = Flask(__name__)
db = client['empleos']
collection = db.empleos

@app.route('/empleos', methods=['GET'])
def get_all_stars():
        output = []
        for s in collection.find():
                # print(list(s))
                output.append({'title': s['title'], 'description_emprsa': s.get('description_emprsa', ""),
                        'country': s.get('country', ""), 'level': s.get('level', ""),'requisitos': s.get('requisitos', ""),
                        'beneficios': s.get('beneficios', "")})
        return jsonify({'result': output})


@app.route('/empleos/<categoria>', methods=['GET'])
def get_by_categoria(categoria):
        filter = {'category': categoria}
        output = []
        for s in collection.find(filter):
                # print(s)
                output.append({'title': s['title'], 'description_emprsa': s.get('description_emprsa', ""),
                        'country': s.get('country', ""), 'level': s.get('level', ""),'requisitos': s.get('requisitos', ""),
                        'beneficios': s.get('beneficios', "")})
        return jsonify({'result': output})


app.run(debug=True)







