from csv import DictReader


def read_csv_data(datafile):
    wallet = []
    with open(datafile, 'r') as datafile:
        datas = DictReader(datafile, delimiter=',')
        header = datas.fieldnames
        for data in datas:
            action_yield = round(float(data[header[1]])*(float(data[header[2]])/100), 2)
            if action_yield > 0:
                wallet.append((data[header[0]], float(data[header[1]]), action_yield))
    return wallet
