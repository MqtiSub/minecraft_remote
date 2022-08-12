from mcje.minecraft import Minecraft
import param_MCJE as param
import numpy as np
#引数が(x,z,y)とかいう変な順番なので気を付けて
#CAUTION!! PUT IN (x,z,y)...
def setCircle(mc,ca,cb,cc,radius,block):
    i=0
    a=300
    if radius <= 15:
        a = 100
    rad=np.linspace(0,2*np.pi,a)
    while i < a:
        cx=radius*np.cos(rad[i])
        cz=radius*np.sin(rad[i])
        cx=int(cx)
        cz=int(cz)
        mc.setBlock(cx+ca,cc,cz+cb,block)
        i += 1

if __name__ == '__main__':
    mc = Minecraft.create(port=param.PORT_MC)
    setCircle(mc,-82,142,59,13,param.LIME_CONCRETE)
