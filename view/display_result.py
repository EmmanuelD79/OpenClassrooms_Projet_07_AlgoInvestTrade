def display_result(result, wallet):
    """
    Affichage dans le terminal du résultat de l'algorithme

    :param result: tuple avec le résultat à afficher
    :param wallet: tuple contenant l'ensemble des actions

    """
    nb_shares_wallet = len(wallet)
    shares_selected, result_price, result_yield = result[0][0]
    method_name, method_time = result[1]
    nb_shares = len(shares_selected)

    selected_string = " a été sélectionné"
    if nb_shares > 1:
        selected_string = "s ont été sélectionné"
    msg = f"{nb_shares} action{selected_string} pour un montant de {str('{:.2f}'.format(result_price)):>6s}€"

    seconde = ""
    if method_time > 1:
        seconde = "s"
    msg_time = f"L'algorithme {method_name} a mis {method_time} seconde{seconde}"

    max_length_string = max(len(msg), len(msg_time))
    print("=" * max_length_string)
    print(("Methode " + method_name + " sur " + str(nb_shares_wallet) + " actions").center(max_length_string))
    print("=" * max_length_string)
    share_msg = f"Liste des {len(shares_selected)} actions sélectionnées"
    print(share_msg.center(max_length_string))
    print("=" * max_length_string)

    for share in shares_selected:
        share_name, share_price, share_yield = share
        print(f"{share_name:<10s} "
              f"(prix: {str('{:.2f}'.format(share_price)):>6s}€, "
              f"rendement: {str('{:.2f}'.format(share_yield)):>6s}€)")

    print("=" * max_length_string)
    print(f"Le rendement sur 2 ans est de {str('{:.2f}'.format(result_yield))}€")
    print("=" * max_length_string)
    print(msg)
    print(msg_time)

    return display_result
