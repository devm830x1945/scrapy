
from flask import Flask
from flask import jsonify
from engien.config import client


app = Flask(__name__)

db = client['empleos']
collection = db.empleos


@app.route('/empleos', methods=['GET'])
def get_all_stars():
  output = []
  for s in collection.find({}):
    print(s)
    output.append({'title' : s['title'], 'description' : s['description_emprsa']})
  return jsonify({'result' : output})

@app.route('/empleos/<categoria>', methods=['GET'])
def get_by_categoria(categoria):
  filter = {'category' : categoria}
  output = []
  print(list(s))
  for s in collection.find(filter):
    print(s)
    output.append({'title' : s['title'], 'description' : s['description_emprsa']})
  return jsonify({'result' : output})

