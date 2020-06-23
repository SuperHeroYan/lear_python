back_pack = {'rope':2, 'arrows':5, 'dagger':1, 'gold coin':228}

def show_inventory(staff):
    
    print('Inventory:')
    item_total = 0

    for k, v in staff.items():
        print(str(k) + ' ' + str(v))
        item_total += int(v)

    print('Total number of items: ' + str(item_total))

def add_to_inventory(staff, add_items):
    invent = staff

    for i in add_items:
        invent.setdefault(i, 0)
        invent[i] += 1
    
    show_inventory(invent)

add = ['gold coin', 'dagger', 'gold coin']

add_to_inventory(back_pack, add)