the_inventory = {'ration' : 8, 'caltrop' : 12}
added_items = ['eye of vecna', 'ration', 'ration']

def print_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print("Total number of items: ", item_total)

def add_to_inventory(inventory, added_items):
    print('Adding', added_items, 'to', inventory)
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    print_inventory(inventory)

add_to_inventory(the_inventory, added_items)
