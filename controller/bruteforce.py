from utils.wrappers.count_time import count_time


@count_time
def bruteforce(wallet, max_amount, rounding=1):
    """
    Algorithme bruteforce de recherche d'actions pour un meilleur rendement

    :param wallet: portefeuille à optimiser
    :param max_amount: la somme maximale de l'investissement
    :return: Tuple des actions sélectionnées pour le meilleur rendement
    """
    lst_shares_result = ()
    nb_shares = len(wallet)
    yield_max = 0
    price_max = 0
    iteration = 0
    for int_combination in range(1, pow(2, nb_shares)):
        sum_yield = 0
        sum_price = 0
        shares_selected = []
        combination_converted_binary = format(int_combination, str(nb_shares) + 'b')

        for index, bit in enumerate(combination_converted_binary):
            if bit == "1":
                share_name, share_price, share_yield = wallet[index]
                sum_price += share_price
                sum_yield += share_yield
                shares_selected.append((share_name, share_price, share_yield))
            iteration += 1

        if sum_price <= max_amount and sum_yield >= yield_max:
            price_max = round(sum_price, 2)
            yield_max = round(sum_yield, 2)
            lst_shares_result = tuple(shares_selected)

    return (lst_shares_result, price_max, yield_max), iteration
