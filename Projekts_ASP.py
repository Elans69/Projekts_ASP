import random
# funckija lai varētu izmantot random atribūtu

# veidojam inputu, kur lietotājs ieraksta savu izvēli ar nepaeizās izvēlēs labošanu
def lietotaja_izvele():
    choice = input("Ieraksti savu izvēli (akmens, papīrs, vai šķēres): ").strip().lower()
    while choice not in ['akmens', 'papīrs', 'šķēres']:
        print("Nepareiza izvēle! Lūdzu ieraksti akmens, papīrs, vai šķēres.")
        choice = input("Ieraksti savu izvēli (akmens, papīrs, vai šķēres): ").strip().lower()
    return choice

# veidojam funkciju kur tiek random ģenerēta "datora
def datora_izvele():
    """Generate the computer's random choice"""
    return random.choice(['akmens', 'papīrs', 'šķēres'])

# veidojam funkciju, kur tiek izmantots if, elif, else, lai atšķirība no rezultāta varētu noteikt uzvarētāju
def kurs_uzvareja(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Neizšķirts"
    elif (player_choice == 'akmens' and computer_choice == 'šķēres') or \
         (player_choice == 'papīrs' and computer_choice == 'akmens') or \
         (player_choice == 'šķēres' and computer_choice == 'papīrs'):
        return "Tu uzvarēji!"
    else:
        return "Dators uzvarēja!"

# galvenā spēles funkcija, kur tiek skaitīts datora un lietotāja punktus, kā arī intro un outro tekstu, kad lietotājs palaiž terminālu un beidz spēli
    # izmantojot if, elif un in range, var pareizi saskaitīt un aprēķināt uzvarētāju
def spele():
    print("Esi laipni lūgts spēle akmens-šķēres-papīrs!")
    num_rounds = int(input("Cik reizes vēlies spēlēt: "))
    player_score = 0
    computer_score = 0

    for round_num in range(1, num_rounds + 1):
        print(f"\nkārta {round_num}:")
        player_choice = lietotaja_izvele()
        computer_choice = datora_izvele()
        print(f"Dators izvēlējās: {computer_choice}")
        result = kurs_uzvareja(player_choice, computer_choice)
        print(result)

        if "Tu uzvarēji" in result:
            player_score += 1
        elif "Dators uzvarēja" in result:
            computer_score += 1

    print("\nSpēle beidzās!")
    print(f"Skaits: Lietotājs {player_score} - {computer_score} Dators")
    if player_score > computer_score:
        print("Apsveicu, tu uzvarēji!")
    elif player_score < computer_score:
        print("Dators uzvarēja :(")
    else:
        print("Ir neizšķirts, mēģini atkal!")

# Galvenā funkcija, lai spēle sāktos
spele()
