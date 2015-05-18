import math
import bpy
import bge
cont = bge.logic.getCurrentController()
obj = cont.owner
default = False
chunks = 64
world_list = []

def chunk_sort(chunks1):
#this does a good amount of math m8
    total_chunks = chunks1
    if (x ** 2) == total_chunks:
        xrows = math.sqrt(total_chunks)
        yrows = math.sqrt(total_chunks)
        Xoffset = xrows * (xrows - 1)
        Yoffset = Xoffset
#now lets make the table list for chunks
    Chunk_List = []
    for x in range(1,total_chunks+1):
        xcord = Xoffset + ((x % xrows) * 8)
        ycord = Yoffset + ((x / yrows) // 1) * 8)
        Chunk_List.append([xcord, ycord])
    return Chunk_List

def make_village(num):
    village1 = [#This is a standard rock village house from 0 on zed
    3,3,3,3,3,3,3,3,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    ]
    village2 = [
    3,3,3,3,3,3,3,3,
    0,5,5,5,5,5,5,0,
    0,5,5,5,5,5,5,0,
    0,5,5,5,5,5,5,0,
    0,5,5,5,5,5,5,0,
    0,5,5,5,5,5,5,0,
    0,5,5,5,5,5,5,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0
    ]
    village3 = [
    3,3,3,3,3,3,3,3,
    0,5,5,5,5,5,5,0,
    0,5,0,0,0,0,5,0,
    0,5,0,0,0,0,5,0,
    0,5,0,0,0,0,5,0,
    0,5,0,0,0,0,5,0,
    0,5,5,5,5,5,5,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0
    ]
    village4 = [
    3,3,3,3,3,3,3,3,
    0,5,5,5,5,5,5,0,
    0,5,0,0,0,0,5,0,
    0,5,0,0,0,0,5,0,
    0,5,0,0,0,0,5,0,
    0,5,0,0,0,0,5,0,
    0,5,5,5,5,5,5,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    ]
    village5 = [
    3,3,3,3,3,3,3,3,
    0,5,5,5,5,5,5,0,
    0,5,0,0,0,0,5,0,
    0,5,0,0,0,0,5,0,
    0,5,0,0,0,0,5,0,
    0,5,0,0,0,0,5,0,
    0,5,5,5,5,5,5,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    ]
    village6 = [
    3,3,3,3,3,3,3,3,
    0,5,5,5,5,5,5,0,
    0,5,0,0,0,0,5,0,
    0,5,0,0,0,0,5,0,
    0,5,0,0,0,0,5,0,
    0,5,0,0,0,0,5,0,
    0,5,5,5,5,5,5,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    ]
    village7 = [
    3,3,3,3,3,3,3,3,
    0,5,5,5,5,5,5,0,
    0,5,5,0,0,5,5,0,
    0,5,5,0,0,5,5,0,
    0,5,5,5,5,5,5,0,
    0,5,5,5,5,5,5,0,
    0,5,5,5,5,5,5,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    ]
    village8 = [
    3,3,3,3,3,3,3,3,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    ]
    if num == 1:
        return village1
    if num == 2:
        return village2
    if num == 3:
        return village3
    if num == 4:
        return village4
    if num == 5:
        return village5
    if num == 6:
        return village6
    if num == 7:
        return village7
    if num == 8:
        return village8

def write_unit(biome_control, flatworld_control):
    biome = 1
    if biome_control == False:
        biome_chance = randint(1, 30)
    Unit_List = []
    if flatworld_control == False and biome == 1:#This is grass biome
        for x in range(64):
            Terrain_List = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
             for y in range(8):
                Unit_List[x][y] = []
                random_chance = randint(1, 100)
                if x == 0:
                    Unit_List[x][y].append(1)
                if x > 0 and x < 32:#This is for ores

                    if random_chance in range(1, 60):#Cold, hard stone!
                        Unit_List[x][y].append(5)

                    if random_chance in range(60, 70):#Iron!
                        Unit_List[x][y].append(9)

                    if random_chance in range(70, 74):#Tin!
                        Unit_List[x][y].append(8)

                    if random_chance in range(74, 79):#Aluminum!
                        Unit_List[x][y].append(10)

                    if random_chance in range(79, 84):#Copper gets it done!
                        Unit_List[x][y].append(7)

                    if random_chance in range(84, 88) and x > 0 and x < 18:#Gold, Gold, Gold!
                        Unit_List[x][y].append(11)

                    if random_chance in range(88, 89) and x > 0 and x < 16 and biome in range(25, 30):#Spooky Dark Crystals!
                        Unit_List[x][y].append(15)

                    if random_chance in range(89, 90) and x > 0 and x < 8:#Emerald!
                        Unit_List[x][y].append(13)

                    if random_chance in range(90, 94) and x > 0 and x < 24:#Thyrumite!
                        Unit_List[x][y].append(14)

                    if random_chance in range(94, 99):#Good ol' Coal!
                        Unit_List[x][y].append(6)

                    if random_chance in range(99, 101) and x > 0 and x < 8:#Diamonds!
                        Unit_List[x][y].append(12)
                if x >= 32:

                    if village_chance == 1:#This makes the village primitive
                        make_village(y)
                    if x == 32:
                        if Terrain_List[y] > 1:
                            Unit_List[x][y].append(4)
                            Terrain_List[y] -= 1

                        if Terrain_List[y] == 1:
                            Unit_List[x][y].append(5)
                            Terrain_List[y] -= 1

                        if Terrain_List[y] >= 0:
                            Unit_List[x][y].append(0)
#sinChange = math.sin(chunks)
#world_slope = math.sin(math.radians(x))
#And Finally...
        world_list.append(Unit_List)
def render_world_by_list(world_list, coords_list):#


def coord_plane_render_sort(direct, val, coords, prex, prey, prez):
    x = (coords - 7) + (prex * 2)
    y = (coords - 7) + (prey * 2) 
    z = -64 + (prez*2)

    if direct == “+X”:
        scene.addObject(val “+X”, “spawner”).worldPosition(x, y, z)

    if direct == “-X”:
        scene.addObject(val + “-X”, “spawner”).worldPosition(x, y, z)

    if direct == “+Y”:
        scene.addObject(val + “+Y”, “spawner”).worldPosition(x, y, z)

    if direct == “-Y”:
        scene.addObject(val +“-Y”, “spawner”).worldPosition(x, y, z)

    if direct == “+Z”:
        scene.addObject(val +”+Z”, “spawner”).worldPosition(x, y, z)

    if direct == “-Z”:
        scene.addObject(val +“-Z”, “spawner”).worldPosition(x, y, z)
def val_sort(val):
    if val == -1:
        return 
    if val == 0:
    if val == 1:
    if val == 2:
    if val == 3:
    if val == 4:
    if val == 5:
    if val == 6:
    if val == 7:
    if val == 8:
    if val == 9:
   if val == 10:
   if val == 11:

#
def initial_render_list(WorldList, UnitList):
    for i in range(len(WorldList)):
        coords = UnitList[i]
        for y in range(len(WorldList[i])):
            for x in range(len(WorldList[i][y]):
                z = x//8
                if WorldList[i][y][x] == 0 or WorldList[i][y][x] < 32:
                    pass
                else:
                        if WorldList[i][y][x+1] !=0:
                            coord_plane_render_sort("+X", WorldList[i][y][x], coords, 2x, 2y, 2z)
                        if WorldList[i][y][x-1] !=0:
                           coord_plane_render_sort("-X", WorldList[i][y][x], coords, 2x, 2y, 2z)
                        if WorldList[i][y][x+8] !=0:
                           coord_plane_render_sort("+Z", WorldList[i][y][x], coords, 2x, 2y, 2z)
                        if WorldList[i][y][x-8] !=0:
                           coord_plane_render_sort("-Z", WorldList[i][y][x], coords, 2x, 2y, 2z)
                        if WorldList[i][y+1][x] !=0:
                            coord_plane_render_sort("+Y", WorldList[i][y][x], coords, 2x, 2y, 2z)
                        if WorldList[i][y-1][x-8] !=0:
                            coord_plane_render_sort("-Y", WorldList[i][y][x], coords, 2x, 2y, 2z)

