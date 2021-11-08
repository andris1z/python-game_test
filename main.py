import random
import time
import os
from inventory import Item, add_health_potion, add_item_to_inv, add_pistol_ammo, ammo_count, damage_player, inventory_array, inv_test, print_inv, print_usuables, playerHP, playerGold, playerMaxHP, use_item

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def print_hp_bar(hp, max_hp):
    print("[", end="") 
    print("❤️ "*hp, end="")
    print("🖤"*(max_hp-hp), end="")
    print("]", end="")
    print(f" Health: [{hp}/{max_hp}]")

def print_player_gold():
    print(f"Gold: {playerGold}💰")

def add_player_gold(amount):
    global playerGold
    playerGold = playerGold + amount

def fight_monster():

    whosTurn = 1 # 1 - player turn, 2 - enemy turn
    EnemyHealth = random.randint(20, 25)
    EnemyAttack = random.randint(1, 3)

    print("_______________________________________________")
    time.sleep(0.5)
    print("_______________________________________________")
    time.sleep(0.5)
    print("_______________________________________________")
    time.sleep(0.5)
    print("_______________________________________________")
    time.sleep(0.5)
    print("_______________________________________________")
    time.sleep(0.5)
    print("_______________________________________________")
    time.sleep(0.5)
    print("_______________________________________________")

    cls()

    while EnemyHealth > 0:
        cls()

        from inventory import playerHP, playerMaxHP
        print_hp_bar(playerHP, playerMaxHP)
        print_player_gold()
        print(f"{ammo_count()}\n")

        print("_______________________________________________")
        print(f"Test Enemy, HP {EnemyHealth}, ATK {EnemyAttack}")

        if whosTurn == 1:

            action = input("""Choose your action
[ATTACK]
[USE ITEM]
""")
            if action == "ATTACK" or action == "USE ITEM":
                if action == "ATTACK":
                    rndDamage = random.randint(3, 8)
                    EnemyHealth = EnemyHealth - rndDamage
                    if EnemyHealth < 1:
                        print(f"You've dealt {rndDamage} DMG to enemy, he has 0 HP left, therefore killing him")
                    else:
                        print(f"You've dealt {rndDamage} DMG to enemy, he has {EnemyHealth} HP left")
                    add_pistol_ammo(-1, 1)
                    whosTurn = 2
                    time.sleep(2)
                if action == "USE ITEM":
                    print_usuables()
                    whosTurn = 2
                    input("Press Enter to continue")

        if whosTurn == 2 and EnemyHealth > 0:
            rndDamage = random.randint(1, EnemyAttack)
            damage_player(rndDamage)
            from inventory import playerHP, playerMaxHP
            if playerHP < 0:
                print(f"The enemy attacks you and deals you {rndDamage} DMG, therefore killing you...")
                exit()
            else:
                print(f"The enemy attacks you and deals you {rndDamage} DMG, you have {playerHP} HP left")
            input("Press Enter to continue")
            whosTurn = 1


# MAIN GAME LOOP

while True:
    if playerHP < 1:
        print("Game over....")
        exit()

    from inventory import playerHP, playerMaxHP
    print_hp_bar(playerHP, playerMaxHP)
    print_player_gold()
    print(f"{ammo_count()}\n")

    print("""Choose your action:
[INVENTORY]
[EXPLORE]""")
    wantsAction = True
    while wantsAction:
        action = input("")
        if action == "INVENTORY" or action == "EXPLORE":
            if action == "INVENTORY":
                wantsAction = False
                wantsInv = True
                while wantsInv:
                    invAction = input("[USE ITEM] or [INVENTORY] ?")
                    if invAction == "USE ITEM" or invAction == "INVENTORY":
                        if invAction == "USE ITEM":
                            wantsInv = False
                            use_item()
                        if invAction == "INVENTORY":
                            wantsInv = False
                            print_inv()
                input("Press Enter to continue")
            if action == "EXPLORE":
                wantsAction = False
                shouldFindMonster = random.randint(1, 1000)
                if (shouldFindMonster < 200):
                    print("You find a monster!")
                    time.sleep(3)
                    cls()
                    fight_monster()
                else:
                    findLoot = random.randint(1, 1000)
                    if findLoot <= 333:
                        print("You find nothing")
                    if findLoot > 333:
                        if findLoot <= 1000 and findLoot >= 778: # gold found
                            goldFound = random.randint(10, 42)
                            print(f"You find {goldFound}x gold")
                            add_player_gold(goldFound)
                        if findLoot < 778 and findLoot >= 556: # ammo
                            ammoFound = random.randint(1, 10)
                            print(f"You find {ammoFound}x ammo")
                            add_pistol_ammo(ammoFound, 1)
                        if findLoot < 556 and findLoot > 333: # potions
                            potionsFound = random.randint(1, 3)
                            print(f"You find {potionsFound}x potions")
                            add_health_potion(potionsFound, 1)

        else:
            print("Invalid Input")
            time.sleep(3)

    time.sleep(1)
    cls()