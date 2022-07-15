import param_MCJE as param
import time
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

class creeper_ex():

    def __init__(self,mc,x,y,z):
        self.mc = mc
        self.x = x
        self.y = y
        self.z = z
        self.mc.setBlocks(self.x,self.y,self.z,self.x+FACE_FLAME,self.y-FACE_FLAME,self.z+FACE_FLAME,param.LIME_CONCRETE)
        self.mc.postToChat("x -> ~"+str(FACE_FLAME)+",y -> ~-"+str(FACE_FLAME)+",z -> ~"+str(FACE_FLAME)+", "+str(FACE_FLAME)+"^3 cube")
    
    def creeper_set(self,var,neg,code,head_block="coal_block",parts_block="lime_concrete"):
        self.mc.setBlocks(self.x,self.y,self.z,self.x+FACE_FLAME,self.y-FACE_FLAME,self.z+FACE_FLAME,head_block)
        line_offset = 0
        for line in creeper_design:
            dot_offset = 0
            for dot in line:
                if dot == '0':
                    block_color_id = head_block
                else:
                    block_color_id = parts_block
                
                if var == 'x':
                    self.x =+ dot_offset*code
                elif var == 'y':
                    self.y =+ dot_offset*code
                elif var == 'z':
                    self.z =+ dot_offset*code
                
                if neg == 'x':
                    self.x =- line_offset
                elif neg == 'y':
                    self.y =- line_offset
                elif neg == 'Z':
                    self.z =- line_offset
                
                self.mc.setBlock(self.x,self.y,self.z,block_color_id)
                dot_offset =+ 1
            line_offset =+ 1

    def creeper_turn(self):
        self.creeper_set('x','y',POSITIVE)
        time.sleep(0.2)
        self.creeper_set('z','y',NEGATIVE)
        time.sleep(0.2)
        self.creeper_set('x','y',NEGATIVE)
        time.sleep(0.2)
        self.creeper_set('z','y',POSITIVE)
        time.sleep(0.2)
        #At the same point,it starts.YOU NEED NOT CHANGE THE POINT.
        self.creeper_set('z','x',POSITIVE) 
        time.sleep(0.2)
        self.creeper_set('x','z',NEGATIVE)
