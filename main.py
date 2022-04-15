import time
import calendar

import requests
import json

import glob
import os

from pathlib import Path


def get_data():
    r = requests.get('https://api.cartola.globo.com/mercado/selecao')
    # print(r.json())

    gmt = time.gmtime()
    ts = calendar.timegm(gmt)
    print("timestamp:", ts)

    with open(f'arquivos/{ts}.json', 'w') as jsonfile:
        json.dump(r.json(), jsonfile)

    get_file_list()


def get_file_list():
    return glob.glob("arquivos/*.json")


def get_file_content(path):
    f = open(path)
    content = json.load(f)

    return content


def list_timelapse():
    output = {}

    files = get_file_list()
    for file in files:
        file_name = Path(file).stem
        file_content = get_file_content(file)

        output[file_name] = file_content

    with open(f'compilado/09042022.json', 'w') as jsonfile:
        json.dump(output, jsonfile)

    return output


def runner():
    while True:
        get_data()
        list_timelapse()
        time.sleep(60 * 5)


if __name__ == '__main__':
    runner()
