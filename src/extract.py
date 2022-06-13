from src.constants import *
import requests
import os
import zipfile

def create_destination_paths(destination):
    raw_path = os.path.join(destination, "raw")
    tables_path = os.path.join(destination, "tables")

    for i in range(NUMBER_FILE):
        unzip_path = os.path.join(destination, "tables/table{}".format(i + 1))

    try:
        os.makedirs(raw_path)
        os.makedirs(tables_path)
        os.makedirs(unzip_path)

    except FileExistsError:
        pass

    return raw_path, tables_path


def extract(destination="./data"):

    raw_path, tables_path = create_destination_paths(destination)

    for file_name, source_url in SOURCE_URLS.items():
        download_file(
            source_url,
            os.path.join(raw_path, file_name)
        )
    unzip_file()

def download_file(url, address):
    # faz a requisicao ao servidor
    response = requests.get(url)

    if response.status_code == requests.codes.OK:
        with open(address, 'wb') as new_file:
            new_file.write(response.content)
    else:
        response.raise_for_status()

def unzip_file():

    for i in range(NUMBER_FILE):
        with zipfile.ZipFile('data/raw/conjunto{}.zip'.format(i + 1), "r") as zip_ref:
            zip_ref.extractall("data/tables/table{}".format(i + 1))
