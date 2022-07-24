import math
import numpy
import time
from mcje.minecraft import Minecraft
import param_MCJE as param
FACE_FLAME = 8
POSITIVE = 1
NEGATIVE = -1
creeper_design = [
    '        ',
    '        ',
    ' 00  00 ',
    ' 00  00 ',
    '   00   ',
    '  0000  ',
    '  0000  ',
    '  0  0  ',
]

    
def creeper_set(mc,x,y,z,var,neg,code,cube_core,head_block=param.GOLD_BLOCK,parts_block=param.LIME_CONCRETE):
    if var == 'x' and neg == 'y' or var == 'y' and neg == 'x':
        Zlength = numpy.sign(cube_core['z'] - z)*FACE_FLAME
    elif var == 'z' and neg == 'y' or var == 'y' and neg == 'z':
        Xlength = numpy.sign(cube_core['x'] - x)*FACE_FLAME
    elif var == 'x' and neg == 'z' or var == 'z' and neg =='x':
        Ylength = numpy.sign(cube_core['y'] - y)*FACE_FLAME
    line_offset = 0 ; once = True
    Ax,Ay,Az = x,y,z
    for line in creeper_design:
        dot_offset = 0
        for dot in line:
            if dot == '0':
                block_color_id = param.GLASS
            else:
                block_color_id = param.IRON_BLOCK
            
            if var == 'x':
                Ax = x + dot_offset*code
                Xlength = FACE_FLAME*code
            if var == 'y':
                Ay = y + dot_offset*code
                Ylength = FACE_FLAME*code
            if var == 'z':
                Az = z + dot_offset*code
                Zlength = FACE_FLAME*code
            
            if neg == 'x':
                Ax = x - line_offset
                Xlength = -FACE_FLAME
            if neg == 'y':
                Ay = y - line_offset
                Ylength = -FACE_FLAME
            if neg == 'z':
                Az = z - line_offset
                Zlength = -FACE_FLAME
            if once == True:
                mc.setBlocks(x,y,z,x + Xlength,y + Ylength,z + Zlength,head_block)
                once = False
            mc.setBlock(Ax,Ay,Az,block_color_id)
            dot_offset =+ 1
        line_offset =+ 1
    time.sleep(5)
    mc.setBlocks(x,y,z,x + Xlength,y + Ylength,z + Zlength,param.AIR)

def creeper_turn(mc,x,y,z):
    cube_core = {'x':x + math.ceil(FACE_FLAME/2),
                 'y':y - math.ceil(FACE_FLAME/2),
                 'z':z - math.ceil(FACE_FLAME/2),}
    mc.postToChat("x -> ~"+str(FACE_FLAME)+",y -> ~-"+str(FACE_FLAME)+",z -> ~"+str(FACE_FLAME)+", "+str(FACE_FLAME)+"^3 cube")
    Ax = x ; Ay = y ; Az = z
    print(Ax,Ay,Az)
    creeper_set(mc,Ax,Ay,Az,'x','y',POSITIVE,cube_core)
    time.sleep(0.2)
    Ax =+ FACE_FLAME
    print(Ax,Ay,Az)
    creeper_set(mc,Ax,Ay,Az,'z','y',NEGATIVE,cube_core)
    time.sleep(0.2)
    Az =- FACE_FLAME
    print(Ax,Ay,Az)
    creeper_set(mc,Ax,Ay,Az,'x','y',NEGATIVE,cube_core)
    time.sleep(0.2)
    Ax = Ax - FACE_FLAME
    print(Ax,Ay,Az)
    creeper_set(mc,Ax,Ay,Az,'z','y',POSITIVE,cube_core)
    time.sleep(0.2)
    Ax =+ FACE_FLAME
    creeper_set(mc,Ax,Ay,Az,'z','x',POSITIVE,cube_core) 
    time.sleep(0.2)
    Ay =- FACE_FLAME ; Az = Az + FACE_FLAME
    creeper_set(mc,Ax,Ay,Az,'x','z',NEGATIVE,cube_core)

if __name__ == '__main__':
    mc = Minecraft.create(port=param.PORT_MC)
    for _ in creeper_design:
        for a in _:
            print(a)
    creeper_turn(mc,0,80,0)