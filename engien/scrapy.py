from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


opts = Options()
opts.add_argument('headless')


browser = Chrome(opts=opts)

def get_listing():
    LIST_CATEGORIES = []
    browser.get('https://www.getonbrd.com.pe/empleos/')
    for i in browser.find_elements_by_xpath("//a[@class='mx-3']"):
        print(i.get_attribute('href'))
        LIST_CATEGORIES.append(i.get_attribute('href'))
    return LIST_CATEGORIES


def get_all_links():
    X = []
    TODO = get_listing()
    for j in TODO:
        browser.get(j)
        for i in browser.find_elements_by_xpath("//a[@data-turbolinks='false']"):
            #print(i.get_attribute('href'))
            X.append(i.get_attribute('href'))
    return X


def parse(url):



    d = dict()

    d['category'] = url.split('/')[-2]

    browser.get(url)

    for i in browser.find_elements_by_xpath("//span[@itemprop='title']"):
        d['title'] = i.get_attribute('innerHTML')
        break

    for i in browser.find_elements_by_xpath("//div[@class='mb4']"):
        try:
            for j in i.find_elements_by_class_name("//div[@class='graphite']"):
                cadena_feature = j.get_attribute('innerHTML')
                if str(cadena_feature).lower() == 'beneficios' or str(cadena_feature).lower() == 'benefits':
                    d['beneficios'] = j.get_attribute('innerHTML')
                else:
                    d['requisitos'] = j.get_attribute('innerHTML')
                break
        except:
            # Descripcion de la empresa
            d['description_emprsa'] = i.get_attribute('innerHTML')
            break
            #Verificar que sea beneficios o requisitos


    for i in browser.find_elements_by_xpath("//span[@itemprop='addressCountry']"):
        d['country'] = i.get_attribute('innerHTML')
        break

    for i in browser.find_elements_by_xpath(".//span[@class='fake-hidden size-3']"):
        #print(i.get_attribute('innerHTML'))
        #print('-----')
        #print(i)
        d['level'] = i.get_attribute('innerHTML')
        break

    # Expresiones regulares para obtener los requisitos, beneficios y descripcion del empleo
    for i in browser.find_elements_by_xpath(".//h3[@class='graphite']"):
        i.get_attribute('innerHTML')
        break

    for i in browser.find_elements_by_xpath(".//h3[@class='graphite']"):
        i.get_attribute('innerHTML')
        break

    return d