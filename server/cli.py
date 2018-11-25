
from server.index import app
from engien import get_all_links, parse
from engien import client
import argparse

def main():
    parser = argparse.ArgumentParser(prog='paramas')
    parser.add_argument('-u', nargs='?', help='update empleos -u  <y> Si  ')

    args = parser.parse_args()

    collected_inputs = {'u': args.u}

    if collected_inputs['u'] == 'y':
        db = client['empleos']
        collection = db.empleos
        try:
            result = collection.insert_many([i for i in map(parse, get_all_links())])

            print('Success')
        except :
            print('Algo paso')
    else:
        print('No actualiza')

    app.run(debug=True)

