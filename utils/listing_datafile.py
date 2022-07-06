from constants.contants import DATAFILE_DIRECTORY
import os


def listing_datafile():
    items = os.listdir(DATAFILE_DIRECTORY)

    datafile = []
    for names in items:
        if names.endswith(".csv"):
            datafile.append(names)

    return datafile
