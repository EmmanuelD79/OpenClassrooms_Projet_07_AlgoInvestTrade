from utils.listing_datafile import listing_datafile
from utils.validate_input_format import validate_format


def get_file_analyze():
    datafile = listing_datafile()
    if datafile:
        files = {}
        print("\nveuillez choisir un de ces fichiers pour l'analyser\n")
        for index, datafile in enumerate(datafile, start=1):
            files[index] = datafile
            print(f"{index} - {datafile}")
        print("0 - Quitter l'application\n")
        validate = False
        while not validate:
            choice = validate_format("Quel est votre choix ?\n", "[0-9]")
            if int(choice) <= len(files.keys()) and int(choice) > 0:
                return files[int(choice)]
            elif int(choice) == 0:
                exit()
    else:
        print("Aucun fichier de données a été trouvé\n")
        exit()


def get_algo(datafile):

    filename = datafile.split("/")
    print(f"Choisissez un algorithme pour l'analyse du fichier {filename}\n")
    print("1 - Méthode BrutForce")
    print("2 - Méthode Optimisée")
    print("0 - revenir en menu principal\n")
    validate = False
    while not validate:
        choice = validate_format("Quel est votre choix ?\n", "[0-9]")
        if int(choice) > 0 and int(choice) <= 2:
            return int(choice)


def get_options():
    amount_max = validate_format("\nQuel est le montant maximal en euros d'investissement?\n", "[0-9]")
    print("Dans le cas où votre dataset a des nombres décimaux")
    print("Afin d'avoir une meilleure précision dans l'analyse")
    print("veuillez choisir un de ces 3 niveaux de précision.\n")
    print("1 - Nombre entier")
    print("2 - Nombre au dixième")
    print("3 - Nombre au centième")
    validate = False
    while not validate:
        rounding = validate_format("\nQuel est votre choix ?\n", "[0-9]")
        if int(rounding) > 0 and int(rounding) <= 3:
            return amount_max, rounding


def get_display():
    print("Quel type d'affichage désirez-vous ?\n")
    print("1 - Affichage sur le terminal")
    print("2 - Ecriture du résultat sur un fichier .txt")
    print("3 - Affichage sur le terminal et écriture sur un fichier .txt")
    validate = False
    while not validate:
        choice = validate_format("\nQuel est votre choix ?\n", "[0-9]")
        if int(choice) > 0 and int(choice) <= 3:
            return int(choice)


def display_lauch(algo):
    print(f"l'analyse a été lancé avec la méthode {algo}")


def display_ending(algo):
    print(f"l'analyse avec la méthode {algo} est terminée")

def prompt_restart():
    restart = validate_format("Voulez-vous effectuer une nouvelle analyse O/N ?", "(O|N){1}$")
    return restart
