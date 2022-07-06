import matplotlib.pyplot as plt
from controller.bruteforce import bruteforce
from controller.optimized import optimized
from utils.read_csv_dataset import read_csv_data


DICT_ALGO = {1: bruteforce, 2: optimized}


def test_graph(func, datafile, *args):
    wallet = read_csv_data(datafile)
    x = []
    y = []
    for ex in range(1, len(wallet) + 1):
        dataset = wallet[:ex]
        print(f"calcul pour un dataset de {len(dataset)} valeur(s)")
        x.append(len(dataset))
        result = func(dataset, *args)
        y.append(result[0][1])

    plt.figure()
    plt.plot(x, y, label='')
    plt.title(func.__name__)
    plt.xlabel('nb données')
    plt.ylabel('nb operations')

    plt.show()


test_graph(optimized, 'datasets/dataForceBrute.csv', 500)
