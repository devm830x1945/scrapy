from engien.scrapy import get_all_links, parse
from engien.config import client

PROD = True

if __name__ == '__main__':
    pass
    '''if PROD:
        db = client['empleos']
        collection = db.empleos
        try:
            result = collection.insert_many([i for i in map(parse, get_all_links())])

            print('Success')
        except :
            print('Algo paso')
    else:
        pass'''

