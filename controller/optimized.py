from utils.wrappers.count_time import count_time


@count_time
def optimized(wallet, max_amount, rounding_index=1):
    """
    Algorithme optimisé de recherche d'actions pour un meilleur rendement

    :param wallet: portefeuille à optimiser
    :param max_amount: la somme maximale de l'investissement
    :param rounding_index: indice d'arrondissage du calcul 1 = à l'unité, 2 = au dizième, 3= au centième
    :return: la liste des actions à acheter pour le meilleur rendement
    """
    try:
        rounding = {1: 1, 2: 10, 3: 100}
        rounding_index = rounding[rounding_index]
    except KeyError:
        rounding_index = 1

    iteration = 0

    nb_slicing_amount = max_amount * rounding_index
    result_row = [((), 0, 0) for x in range(int(nb_slicing_amount + 1))]
    for share in wallet:
        previous_result_row = list(result_row)
        current_share_name, current_share_price, current_share_yield = share
        rounding_price = round(current_share_price * rounding_index)
        for amount, current_cell_tuple in enumerate(result_row[rounding_price:], start=rounding_price):
            gap = int(amount - rounding_price)
            result_yield = current_share_yield + previous_result_row[gap][2]
            result_price = current_share_price + previous_result_row[gap][1]
            if result_price <= max_amount and result_yield >= current_cell_tuple[2]:
                list_shares = list(previous_result_row[gap][0])
                list_shares.append((current_share_name, current_share_price, current_share_yield))
                result_row[amount] = (tuple(list_shares), round(result_price, 2), round(result_yield, 2))
            iteration += 1

    return result_row[-1], iteration
