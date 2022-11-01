import csv
import os
import pathlib
import pprint


def get_phones():
    path = pathlib.Path.cwd()
    phones_file = os.path.join(path, "phones.csv")

    with open(phones_file) as csvfile:
        list_phones = []
        phones = csv.reader(csvfile, delimiter=';')
        for phone in phones:
            list_phones.append(phone)

    return list_phones

