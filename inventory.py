# ammo list
# ID 1 - Pistol, ID 2 - Rifle, ID 3 - Heavy

# weapon list
# ID 1 - Makarov, ID 2 - SKS, ID 3 - AK-47 Rifle, ID 4 -  M416A7

playerHP = 10
playerMaxHP = 10
playerGold = 0

class Item:
    def __init__(self, name, count, ammo_id = -1, weapon_id = -1, usable = False, consumable_id = -1):
        self.name = name
        self.count = count
        self.ammo_id = ammo_id
        self.weapon_id = weapon_id
        self.usable = usable
        self.consumable_id = consumable_id

    def __str__(self):
        return f'{self.name}, x{self.count}'

ammo1 = Item("Pistol Ammo", 11, 1, -1, False, -1)
ammo2 = Item("Rifle Ammo", 12, 2, -1, False, -1)
ammo3 = Item("Heavy Ammo", 13, 3, -1, False, -1)
consumable1 = Item("Basic Heal Potion", 3, -1, -1, True, 1)

inventory_array = [ammo1, consumable1]

def damage_player(damage):
    global playerHP
    playerHP = playerHP - damage
    print(f"u have {playerHP}")

def inv_test():
    inventory_array.append(ammo1)

def print_inv():
    cik_gars = len(inventory_array)
    if cik_gars > 0:
        for item_nr in range(0, cik_gars):
            print(f'Nr: {item_nr}, {inventory_array[item_nr].name}, x{inventory_array[item_nr].count}')

def add_item_to_inv(Item):
    inventory_array.append(Item)

def ammo_count():
    ret_str = """"""
    cik_gars = len(inventory_array)
    if cik_gars > 0:
        for item_nr in range(0, cik_gars):
            item = inventory_array[item_nr]
            if item.ammo_id > 0:
                ammo_sk = item.count
                if item.ammo_id == 1:  
                    ret_str = ret_str + f"""Pistol Ammo x{ammo_sk}\n"""
                if item.ammo_id == 2:
                    ret_str = ret_str + f"""Rifle Ammo x{ammo_sk}\n"""
                if item.ammo_id == 3:
                    ret_str = ret_str + f"""Heavy Ammo x{ammo_sk}\n"""
    
    return ret_str


def add_pistol_ammo(amount, id):
    cik_gars = len(inventory_array)
    if cik_gars > 0:
        for item_nr in range(0, cik_gars):
            item = inventory_array[item_nr]
            if item.ammo_id == id:
                old_ammo = item.count
                new_count = old_ammo + amount
                inventory_array[item_nr].count = new_count

def add_health_potion(amount, id):
    cik_gars = len(inventory_array)
    if cik_gars > 0:
        for item_nr in range(0, cik_gars):
            item = inventory_array[item_nr]
            if item.consumable_id == id:
                old_count = item.count
                new_count = old_count + amount
                inventory_array[item_nr].count = new_count

def print_usuables():
    ret_str = """"""
    atleastoneusable = False
    cik_gars = len(inventory_array)
    if cik_gars > 0:
        for item_nr in range(0, cik_gars):
            item = inventory_array[item_nr]
            if item.usable == True:
                atleastoneusable = True
                ret_str = ret_str + f'ID: {item_nr}, {inventory_array[item_nr].name}, x{inventory_array[item_nr].count}\n'
            
        if atleastoneusable == False:
            ret_str = "You dont have any usable items..."
        
    return ret_str

def is_valid_consumable(item_id):
    is_it_even_consumable = False
    cik_gars = len(inventory_array)
    if cik_gars > 0:
        item = inventory_array[item_id]
        if item.consumable_id > 0:
            is_it_even_consumable = True
                 
    return is_it_even_consumable

def get_item_count_INTERNAL(item_id):
    ret_val = 0
    cik_gars = len(inventory_array)
    if cik_gars > 0:
        item = inventory_array[item_id]
        if item.consumable_id == id:
                ret_val = item.count
            

    return ret_val

def consume_consumable_INTERNAL_DO_NOT_FUCKING_TOUCH_THIS(item_id):
    count = inventory_array[item_id].count
    if count > 0:
        inventory_array[item_id].count = inventory_array[item_id].count - 1
        
def execute_small_heal_logic():
    global playerHP, playerMaxHP

    if playerHP + 3 > playerMaxHP:
        playerHP = playerMaxHP
    else:
        playerHP = playerHP + 3
    print(f"Your current HP is {playerHP}/{playerMaxHP}")

def use_item():
    print_usuables()
    usables_str = print_usuables()
    if usables_str.startswith("You") == True:
        print("You dont have any usable items...")
        exit()
    else:
        print(usables_str)
        tryingToGetItem = True
        while tryingToGetItem == True:
            item_choose = input("Enter the item ID you want to consume or enter [EXIT] if you dont want to consume an item: ")
            if item_choose == "EXIT":
                return
            isValidInput = False
            if item_choose.isdecimal() == False:
                print("Invalid Input")
            if item_choose.isdecimal() == True:
                isValidInput = True
                item_choose = int(item_choose)
            if isValidInput == True:
                if is_valid_consumable(item_choose) == False:
                    print("Invalid Item/ID")
                if is_valid_consumable(item_choose) == True:
                    tryingToGetItem = False
                    consume_consumable_INTERNAL_DO_NOT_FUCKING_TOUCH_THIS(item_choose)
                    execute_small_heal_logic()
                
                


