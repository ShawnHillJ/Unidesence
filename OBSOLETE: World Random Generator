#New World Generator Script
#-------------------------------------------------------------------------------
# Name:    	World Generator
# Purpose: 	Spawns a World
#
# Author:  	Shawn Hill
# Author:  	Eric Wilkins
# Created: 	14/03/2015
# Copyright:   (c) Shawn and Eric 2015
# Licence: 	<your licence>
# Notes and Cheatsheet!
# Vector((0,0,0)) MOVES THINGS!!!!!!!!!!! YEAAHAHAHHA!
# Print version using bpy
#-------------------------------------------------------------------------------
#Spawning Script Ahead!!!
#This gives all the necessary functions to be inserted
import bpy
import math
import random
import bge
#Now we can give ourselves shortcuts to reduce character count
gl = bge.logic
cont = gl.getCurrentController()
se = gl.getCurrentScene()
obs = se.objects
invisiLayer = [False] *20
invisiLayer[1] = True
trueLayer = [False] *20
trueLayer[0] = True
own = cont.owner
#This is the amount of chunks the world will have. This will be updated to be
#infinite soon.
chunks = 16
heightPos = 50
heightNeg = 1
x = random.randint(heightNeg, heightPos)
heightPosative = 100
heightNegative = 1
Randomizer = random.randint(heightNegative, heightPosative)
world_slope = math.sin(math.radians(x))
add_block = bpy.ops.mesh.primitive_cube_add
sinChange = math.sin(chunks)
default = 1
shadingController = 0
if chunks == 0:
	shadingController == 1
#Now for the Good Stuff. Here is the Base Command.
def main():
	#This checks whether or not if there is a seed input by the user when the world starts
	if World_Start == True and worldGeneratorWithoutUserInput == True:
    	    initialize_world(False)
	elif World_Start == True and worldGeneratorWithoutUserInput == False:
    	    initialize_world(True)
#Then we initialize the rest of the functions below for spawning and set the defaults
def initialize_world(userinput):
	if chunks > 0 and userinput == False:
    	    spawn_chunk(10, default, 0, 1, default)
    	    chunks -= 1
def row_sort(chunkRow, xloc, yloc, zloc):
	xpos = 0
	ypos = 0
	zpos = zloc
	#Y Values
	if chunkRow in range(1, 9):
    	    ypos = yloc + 7
	if chunkRow in range(9, 17):
    	    ypos = yloc + 5
	if chunkRow in range(17, 25):
    	    ypos = yloc + 3
	if chunkRow in range(25, 33):
    	    ypos = yloc + 1
	if chunkRow in range(33, 41):
    	    ypos = yloc - 1
	if chunkRow in range(41, 49):
    	    ypos = yloc - 3
	if chunkRow in range(49, 57):
    	    ypos = yloc - 5
	if chunkRow in range(57, 65):
    	    ypos = yloc - 7
	#Now for X values
	if chunkRow in range(1, 65, 8):
    	    xpos = xloc - 7
	if chunkRow in range(2, 65, 8):
    	    xpos = xloc - 5
	if chunkRow in range(3, 65, 8):
    	    xpos = xloc - 3
	if chunkRow in range(4, 65, 8):
    	    xpos = xloc - 1
	if chunkRow in range(5, 65, 8):
    	    xpos = xloc + 1
	if chunkRow in range(6, 65, 8):
    	    xpos = xloc + 3
	if chunkRow in range(7, 65, 8):
    	    xpos = xloc + 5
	if chunkRow in range(8, 65, 8):
    	    xpos = xloc + 7
	return (xpos, ypos, zpos)

#This function will spawn the chunks along with the ores.
#Here the height of each chunk, which is in blender units, will be generated at random.
def spawn_chunk(Height, sinWave, ChunkData, Randomizer, Biome):
	chunkZrows = 64
	chunkCurrentRow = 0
	xVectorPre = range(chunks)
	xVector = -124 + (xVectorPre * 4)
	yVectorPre = chunks % 8
	yVector2 = yVectroPre * 4
	yVector = -124 - yVector2
	Height = int(round(sinWave * Randomizer))
	#In order to properly spawn ores we must determine the coordinates of the vertices within
	# each chunk so that we can change them I'm the next function.
	#Now we can define the possibility of each ore at certain depths, below the surface, within
	#the chunk and set their coordinates.
	if (height % 2) == 1:
    	    height += 1
	for r in chunkZrows:
    	    chunkCurrentRow += 1
    	    for i in range(-50, Height, 2):
        	        zVector = i
        	        if i in range(-50, Height - 8):
            	chance = range(1, 101)
            	OreRand = random.sample(chance, 1)
            	if OreRand in (1, 60):
                	    add_block(
                    	    location = row_sort(chunkCurrentRow, xVector, yVector, zVector)
                    	    )
                	    ob = bpy.context.object
                	    ob.name = "Stone"
                	    ob.show_name = True
            	if OreRand in (60, 70):
                	    add_block(
                    	        location = row_sort(chunkCurrentRow, xVector, yVector, zVector)
                    	        )
                	    ob = bpy.context.object
                	    ob.name = "IronOre"
                	    ob.show_name = True
            	if OreRand in (70, 74):
                	    add_block(
                    	        location = row_sort(chunkCurrentRow, xVector, yVector, zVector)
                    	        )
                	    ob = bpy.context.object
                	    ob.name = "TinOre"
                	    ob.show_name = True
            	if OreRand in (74, 79):
                	    add_block(
                    	    location = row_sort(chunkCurrentRow, xVector, yVector, zVector)
                    	)
                	ob = bpy.context.object
                	ob.name = "AluminumOre"
                	ob.show_name = True
            	if OreRand in (79, 84):
                	    add_block(
                    	        location = row_sort(chunkCurrentRow, xVector, yVector, zVector)
                    	        )
                	    ob = bpy.context.object
                	    ob.name = "CopperOre"
                	    ob.show_name = True
            	if OreRand in (84, 90):
                	    add_block(
                    	    location = row_sort(chunkCurrentRow, xVector, yVector, zVector)
                    	    )
                	    ob = bpy.context.object
                	    ob.name = "GoldOre"
                	    ob.show_name = True
            	if OreRand in (84, 85):
                	    add_block(
                    	location = row_sort(chunkCurrentRow, xVector, yVector, zVector)
                    	)
                	ob = bpy.context.object
                	ob.name = "Dark Crytal"
                	ob.show_name = True
            	if OreRand in (85, 86):
                	add_block(
                    	location = row_sort(chunkCurrentRow, xVector, yVector, zVector)
                    	)
                	ob = bpy.context.object
                	ob.name = "Emerald"
                	ob.show_name = True
            	if OreRand in (86, 87):
                	add_block(
                    	location = row_sort(chunkCurrentRow, xVector, yVector, zVector)
                    	)
                	ob = bpy.context.object
                	ob.name = "Lapis"
                	ob.show_name = True
            	if OreRand in (87, 90):
                	add_block(
                    	location = row_sort(chunkCurrentRow, xVector, yVector, zVector)
                    	)
                	ob = bpy.context.object
                	ob.name = "Diamond"
                	ob.show_name = True
            	if OreRand in (90, 95):
                	    add_block(
                    	location = row_sort(chunkCurrentRow, xVector, yVector, zVector)
                    	)
                	ob = bpy.context.object
                	ob.name = "Coal"
                	ob.show_name = True
            	if OreRand in (95, 100):
                	    add_block(
                    	location = row_sort(chunkCurrentRow, xVector, yVector, zVector)
                    	)
                	ob = bpy.context.object
                	ob.name = "Thyrumite"
                	ob.show_name = True
            	elif i > Height - 8 and i != Height:
                	add_block(
                    	location = row_sort(chunkCurrentRow, xVector, yVector, zVector)
                    	)
                	ob = bpy.context.object
                	ob.name = "Dirt"
                	ob.show_name = True
            	elif i == Height:
                  	add_block(
                    	location = row_sort(chunkCurrentRow, xVector, yVector, zVector)
                    	)
                  	ob = bpy.context.object
                  	ob.name = "Grass"
                  	ob.show_name = True
#now we execute the spawn function
spawn_chunk(10, default, 0, 1, default)
#spawn_chunk(Height, sinWave, ChunkData, Randomizer, Biome)
#
