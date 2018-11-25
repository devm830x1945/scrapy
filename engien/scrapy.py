from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup as BSoup

import re

opts = Options()
opts.add_argument('headless')


browser = Chrome()



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

def cleaning_text(string):
    return re.sub(r'<[a-zA-Z]*>|</[a-zA-Z]*>', string, ' ')

def parse(url):

    d = dict()

    d['category'] = url.split('/')[-2]

    browser.get(url)

    bs_obj = BSoup(browser.page_source, 'html.parser')


    #for i in browser.find_elements_by_xpath("//strong[@class='company-name']"):
    #    d['company'] = cleaning_text(i.get_attribute('innerHTML'))
    #    break
    for i in bs_obj.find_all("strong", {"class":"company-name"}):
        d['company'] = i.text

    #for i in browser.find_elements_by_xpath("//span[@itemprop='title']"):
    #    d['title'] = cleaning_text(i.get_attribute('innerHTML'))
    #    break
    for i in bs_obj.find_all("span", {"itemprop":"title"}):
        d['title'] = i.text
        break

    #for i in browser.find_elements_by_xpath("//div[@class='mb4']"):
    for i in bs_obj.find_all("div", {"class": "mb4"}):
        try:
            #for j in i.find_elements_by_class_name("//div[@class='graphite']"):
            for j in bs_obj.find_all("h3", {"class": "graphite"}):
                cadena_feature = j.text
                print(cadena_feature)
                print('******************')
                #j.get_attribute('innerHTML')
                if 'beneficios' in str(cadena_feature).lower() or 'benefits' in str(cadena_feature).lower():
                    p = j.find('p')
                    print('*********** >>> ', p)
                    d['beneficios'] = p.text
                    #j.get_attribute('innerHTML')
                else:
                    p = j.find('p')
                    print('*********** >>> ', p)
                    d['requisitos'] = p.text
                    #j.get_attribute('innerHTML')
                break
        except:
            # Descripcion de la empresa
            d['description_emprsa'] = i.text
            #i.get_attribute('innerHTML')
            break
            #Verificar que sea beneficios o requisitos


    #for i in browser.find_elements_by_xpath("//span[@itemprop='addressCountry']"):
    #    d['country'] = i.get_attribute('innerHTML')
    #    break
    for i in bs_obj.find_all("span", {"itemprop":"addressCountry"}):
        d['country'] = i.text
        break

    '''for i in browser.find_elements_by_xpath(".//span[@class='fake-hidden size-3']"):
        #print(i.get_attribute('innerHTML'))
        #print('-----')
        #print(i)
        d['level'] = i.get_attribute('innerHTML')
        break'''
    for i in bs_obj.find_all("span", {"class":"fake-hidden size-3"}):
        d['level'] = i.text
        break



    # Expresiones regulares para obtener los requisitos, beneficios y descripcion del empleo
    #for i in browser.find_elements_by_xpath(".//h3[@class='graphite']"):
    #    i.get_attribute('innerHTML')
    #    break

    #for i in browser.find_elements_by_xpath(".//h3[@class='graphite']"):
    #    i.get_attribute('innerHTML')
    #    break

    return d