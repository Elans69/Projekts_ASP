import random
# funckija lai varētu izmantot random atribūtu

# izveidoju klasi ar krāsām, ko izmantošu pie print 
class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

  # veidojam inputu, kur lietotājs ieraksta savu izvēli ar nepareizās izvēlēs labošanu
def lietotaja_izvele():
    choice = input(bcolors.OKCYAN + "Ieraksti savu izvēli (akmens, papīrs, vai šķēres): " + bcolors.ENDC).strip().lower()
  #ja būs nepareiza izvēle, tiks paziņots, ka nepareiza izvēle un tiks prasīt ierakstīt vēlreiz
    while choice not in ['akmens', 'papīrs', 'šķēres']:
        print(bcolors.OKCYAN + "Nepareiza izvēle! Lūdzu ieraksti akmens, papīrs, vai šķēres." + bcolors.ENDC)
        choice = input(bcolors.OKCYAN + "Ieraksti savu izvēli (akmens, papīrs, vai šķēres): " + bcolors.ENDC).strip().lower()
    return choice

  # veidojam funkciju kur tiek random ģenerēta "datora
def datora_izvele():
    """uztaisam random ģeneratoru"""
    return random.choice(['akmens', 'papīrs', 'šķēres'])

  # veidojam funkciju, kur tiek izmantots if, elif, else, lai atšķirība no rezultāta varētu noteikt uzvarētāju
def kurs_uzvareja(player_choice, computer_choice):
    if player_choice == computer_choice:
        return bcolors.WARNING + "Neizšķirts" + bcolors.ENDC
    elif (player_choice == 'akmens' and computer_choice == 'šķēres') or \
         (player_choice == 'papīrs' and computer_choice == 'akmens') or \
         (player_choice == 'šķēres' and computer_choice == 'papīrs'):
        return bcolors.OKGREEN + "Tu uzvarēji!" + bcolors.ENDC
    else:
        return bcolors.FAIL + "Dators uzvarēja!" + bcolors.ENDC

# galvenā spēles funkcija, kur tiek skaitīts datora un lietotāja punktus, kā arī intro un outro tekstu, kad lietotājs palaiž terminālu un      beidz spēli
    # izmantojot if, elif un in range, var pareizi saskaitīt un aprēķināt uzvarētāju
def spele():
  # spēles intro,kur ir ielūgšanas teksts ar jautājumu cik kārtas spēlēsi
    print(bcolors.OKBLUE + "Esi laipni lūgts spēle akmens-šķēres-papīrs!" + bcolors.ENDC)
    num_rounds = int(input(bcolors.OKBLUE + "Cik reizes vēlies spēlēt: " + bcolors.ENDC))
    player_score = 0
    computer_score = 0

  #uzraksta pēc izvēles, kas ko izvēlējās un kurš izvēlējās
    for round_num in range(1, num_rounds + 1):
        print(f"\nkārta {round_num}:")
        player_choice = lietotaja_izvele()
        computer_choice = datora_izvele()
        print(f"Dators izvēlējās: {computer_choice}")
        result = kurs_uzvareja(player_choice, computer_choice)
        print(result)
  #pēc katras uzvaras tiks pieskaitīs punkts 
        if "Tu uzvarēji" in result:
            player_score += 1
        elif "Dators uzvarēja" in result:
            computer_score += 1

  # kad beidzās visas kārtas, tiek noteikts uzvarētājs ar if, elif un else
    print("\nSpēle beidzās!")
    print(f"Skaits: Lietotājs {player_score} - {computer_score} Dators")
    if player_score > computer_score:
        print(bcolors.OKGREEN + "Apsveicu, tu uzvarēji!" + bcolors.ENDC)
    elif player_score < computer_score:
        print(bcolors.FAIL + "Dators uzvarēja :(" + bcolors.ENDC)
    else:
        print(bcolors.WARNING + "Ir neizšķirts, mēģini atkal!" + bcolors.ENDC)

# Galvenā funkcija, lai spēle sāktos
spele()