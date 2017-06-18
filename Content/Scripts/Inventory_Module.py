import bge
cont = bge.logic.getCurrentController()
own = cont.owner

inventory = [[["",0],["",0],["",0],["",0],["",0]],
             [["",0],["",0],["",0],["",0],["",0]],
             [["",0],["",0],["",0],["",0],["",0]],
             [["",0],["",0],["",0],["",0],["",0]],
             [["",0],["",0],["",0],["",0],["",0]],
             [["",0],["",0],["",0],["",0],["",0]]]
print(inventory)

def add_item(item_name):
    does_exist = False
    for x in range(len(inventory)):
        for y in range(len(inventory[x])):
            if item_name == inventory[x][y][0]:
                inventory[e][f][1] += 1
                does_exist = True
            break
        break
    if does_exist == False:
        for e in range(len(inventory)):
            for f in range(len(inventory[e])):
                if inventory[e][f][1] == 0:
                    inventory[e][f][0] = item_name
                    inventory[e][f][1] += 1
                break
            break

def move_item(source_name,source_value,destination_name,destination_value,source_messenger):
    #source_messenger = "2345"
    x1 = source_messenger[0]
    y1 = source_messenger[1]
    x2 = source_messenger[2]
    y2 = source_messenger[3]
    if source_name == destination_name:
        inventory[x2][y2][1] += source_value
        inventory[x1][y1][0] == ""
        inventory[x1][y1][1] == 0
    else:
        inventory[x1][y1][0] = destination_name
        inventory[x1][y1][1] = destination_value
        inventory[x2][y2][0] = source_name
        inventory[x2][y2][1] = source_value

def craft_item(slot0,slot1,slot2,slot3,product):
    #slot* = "12"
    #product = "whatever"
    index_string = slot0 + slot1 + slot2 + slot3
    for z in range(0,8,2):
        inventory[index_string[0+z]][index_string[1+z]][1] -= 1
        if inventory[index_string[0+z]][index_string[1+z]][1] == 0:
            inventory[index_string[0+z]][index_string[1+z]][0] = ""
    for a in range(len(inventory)):
        for b in range(len(inventory[a])):
            for c in inventory[a][b]:
                if c[0] == "":
                    c[0] = product
                    break
                break
            break
        break

def trash_item(source_pos):
    inventory[source_pos[0]][source_pos[1]][0] = ""
    inventory[source_pos[0]][source_pos[1]][1] = 0




