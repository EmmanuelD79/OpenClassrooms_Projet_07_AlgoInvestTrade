from utils.read_csv_dataset import read_csv_data
from view.display_result import display_result
from controller.bruteforce import bruteforce
from controller.optimized import optimized
from constants.contants import DATAFILE_DIRECTORY
from view.print_to_file import print_to_file
from view.menu import get_algo, \
    get_file_analyze, display_lauch, \
    get_options, display_ending, get_display, prompt_restart


DICT_ALGO = {1: bruteforce, 2: optimized}


def launch_algo():
    restart = "O"
    while restart == "O":
        algo = None
        datafile = None
        while algo is None:
            datafile = get_file_analyze()
            algo = get_algo(datafile)
            options = get_options()

        wallet = read_csv_data(DATAFILE_DIRECTORY + "/" + datafile)
        func = DICT_ALGO[algo]
        display_lauch(func.__name__)
        result = func(wallet, int(options[0]), int(options[1]))
        display_ending(func.__name__)
        type_display = get_display()

        if type_display == 1:
            display_result(result, wallet)
        elif type_display == 2:
            print_to_file(result, wallet, datafile)
        else:
            display_result(result, wallet)
            print_to_file(result, wallet, datafile)
        restart = prompt_restart()
