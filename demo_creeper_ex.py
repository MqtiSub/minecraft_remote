from mcje.minecraft import Minecraft
import param_MCJE as param
from creeper_ex import creeper_set,creeper_turn

x = 0 ; y = 80 ; z= 0
mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat("Cute creeper is creating...")
creeper_turn(mc,x,y,z)
creeper_set(mc,x,y,z,head_block=param.TNT,parts_block=param.REDSTONE_BLOCK)