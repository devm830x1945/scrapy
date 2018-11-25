from server import app
from engien import get_all_links, parse
import argparse


from engien.config import client



def main():
    print('******************')
    parser = argparse.ArgumentParser(prog='paramas')
    parser.add_argument('-u', nargs='?', help='update empleos -u  <y> Si  ')

    args = parser.parse_args()

    collected_inputs = {'u': args.u}

    if collected_inputs['u'] == 'y':
        db = client['empleos']
        collection = db.empleos
        try:
            collection.insert_many([i for i in map(parse, get_all_links())])
            print('Success')
        except :
            print('Algo paso')
    else:
        app.run(debug=True)
        print('No actualiza')


    # import engien







