# -*- coding: utf-8 -*-

import urllib, sys, os, json, logging, random, pprint
from bs4 import BeautifulSoup
import bs4
import collections

logging.basicConfig(format='[%(levelname)s][%(asctime)s]: %(message)s', level=logging.DEBUG)


def openwebsite(url):

    opener = urllib.FancyURLopener({})
    logging.info("Revisando url " +url)
    f = opener.open(url)
    content = f.read()
    return content

def main():
    salida = dict()
    lista_de_matches = []
    year = "2016"

    # logging.info("Página inicial: " +str(num_page))

    url = "http://www.sii.cl/pagina/valores/uf/uf"+year+".htm"
    page = openwebsite(url);
    soup = BeautifulSoup(page);
    toparse = soup.table.tbody;

    matrix = []

    for item in toparse:
        if type(item) == bs4.element.NavigableString:
            continue
        
        dia = int(item.th.contents[0])
        matrix.append([])

        for a in item:
            if type(a) == bs4.element.NavigableString:
                continue

            val = a.contents[0]
            if val == str(dia):
                continue

            if val == u'\xa0':
                val = "0"
            
            val = val.replace(".", "")
            val = val.replace(",", ".")


            matrix[dia-1].append(float(val))

    for dia, obj in enumerate(matrix):
        print dia+1, obj                 

    json.dump(matrix, open(year+".json", "w"))

    return True

main()