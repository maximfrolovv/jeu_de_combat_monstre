import random


def dice(faces):
    return random.randint(1, faces)


nom = input("C'est quoi ton nom ? ")

print(f"Bienvenue, {nom}")
print("Tu as reçu une épée. Bonne chance !")

defaite = 0
player_health = dice(10) + dice(10)
wins = 0
monster_health = dice(10) + dice(10)

while True:
    if player_health <= 0:
        print("Vous êtes mort.")
        defaite += 1
        print(f"Victoires : {wins}")
        print(f"Défaites : {defaite}")
        exit()

    if monster_health <= 0:
        if wins != 0 and wins % 3 == 0:
            print("Vous avez vaincu le boss.")
            monster_health = dice(10) + dice(10)
        else:
            print("Vous avez vaincu le monstre.")
            monster_health = dice(10) + dice(10)
        wins += 1
        print(f"{wins} victoires")
        print(f"{defaite} défaites")

    if wins != 0 and wins % 3 == 0:
        print("Vous rencontrez le boss.")
        boss_health = dice(15) + dice(20)
        print(f"Le boss a {monster_health} hp")
        print(f"Vous avez {player_health} hp")
        print("Attaque(1), Sauve toi(2), Règlements(3), Quitter(4)")
        choice = input("Votre choix : ")
        try:
            choice = int(choice)
        except ValueError:
            print("Non.")
            continue

        if choice == 1:
            print("Attaque !")
            sword_dps = dice(6)
            result = dice(6)
            m_result = dice(5)
            print(f"Ton dé : {result}, Dé du boss : {m_result}")
            if result > m_result:
                monster_health -= sword_dps
                print(f"Vous avez fait {sword_dps} de dommage au boss.")
                print(f"Il reste {monster_health} hp au boss.")
            else:
                print("Attaque non réussie : ton dé était inférieur ou égal à celui du boss.")
        elif choice == 2:
            print("Tu t'es enfui, tu perds 1 hp.")
            player_health -= 1
            print(f"Il te reste {player_health} hp.")
        elif choice == 3:
            print("""Pour réussir un combat,il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire
Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.
Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.
La partie se termine lorsque les points de vie de l’usager tombent sous 0.
L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement = pénalité de 1 point de vie.g""")
        elif choice == 4:
            print("Merci de jouer !")
            exit()
        else:
            print("Choix invalide.")
            continue
    else:
        print("Il y a un monstre.")
        print(f"Le monstre a {monster_health} hp.")
        print(f"Vous avez {player_health} hp.")
        print("Attaque(1), Sauve toi(2), Règlements(3), Quitter(4)")
        choice = input("Votre choix : ")
        try:
            choice = int(choice)
        except ValueError:
            print("non")
            continue

        if choice == 1:
            print("Attaque !")
            sword_dps = dice(6)
            result = dice(6)
            m_result = dice(5)
            print(f"Ton dé : {result}, Dé du monstre : {m_result}")
            if result > m_result:
                monster_health -= sword_dps
                print(f"Vous avez fait {sword_dps} de dommage au monstre.")
                print(f"Il reste {monster_health} hp au monstre.")
            else:
                print("Attaque non réussie : ton dé était inférieur ou égal à celui du monstre.")
        elif choice == 2:
            print("Tu t'es enfui, tu perds 1 hp.")
            player_health -= 1
            print(f"Il te reste {player_health} hp.")
        elif choice == 3:
            print("""Pour réussir un combat,il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire
Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.
Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.
La partie se termine lorsque les points de vie de l’usager tombent sous 0.
L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement = une pénalité de 1 point de vie.""")
        elif choice == 4:
            print("Merci de jouer !")
            exit()
        else:
            print("Choix invalide.")
            continue
