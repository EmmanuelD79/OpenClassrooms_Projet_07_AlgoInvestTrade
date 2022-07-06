import sys
import os
from constants.contants import RESULTS_DIRECTORY
from view.display_result import display_result


def print_to_file(result, wallet, datafile):
    """
    Ecriture dans un fichier .txt du résultat de l'algorithme
    :param result: tuple avec le résultat à écrire dans le fichier
    :param wallet: tuple contenant l'ensemble des actions
    :param datafile: string du nom de fichier Dataset contenant les données fournit à l'algorithme
    """
    os.makedirs(RESULTS_DIRECTORY, exist_ok=True)
    method_name = result[1][0]
    filename = datafile.split(".")
    filename = RESULTS_DIRECTORY + "/" + method_name + "_" + filename[-2] + ".txt"
    original_stdout = sys.stdout
    with open(filename, 'w') as f:
        sys.stdout = f
        display_result(result, wallet)
        sys.stdout = original_stdout
    display_file_create(filename)


def display_file_create(filename):
    filename = filename.split("/")
    print(f"\nLe fichier {filename[-1]} a été créé dans le dossier {'/'.join(filename[:-1])}/")
