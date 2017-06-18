import bge

cont = bge.logic.getCurrentController
own = cont.owner
scene = bge.logic.getCurrentScene

def return_object(x,y,z):
    for obj in scene.objects:
        if obj.worldPosition(x,y,z) == (x,y,z):
            return obj

def add_block(objectName,x,y,z):
    scene.addObject(return_object(x,y,z)).worldPosition(x,y,z)

def delete_block():
    
    scene.endObject(objectName,objectLocation):

