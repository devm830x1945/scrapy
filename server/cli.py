
import argparse






def main():
    print('******************')
    parser = argparse.ArgumentParser(prog='paramas')
    parser.add_argument('-u', nargs='?', help='update empleos -u  <y> Si  ')

    args = parser.parse_args()

    collected_inputs = {'u': args.u}

    if collected_inputs['u'] == 'y':
        from engien.config import client
        from engien.scrapy import get_all_links, parse
        print('No entres!')
        db = client['empleos']
        collection = db.empleos
        try:
            collection.insert_many([i for i in map(parse, get_all_links())])
            print('Success')
        except Exception as e:
            print('Algo paso')
    else:
        from server.server import app
        app.run(debug=True)
        print('No actualiza')


    # import engien







