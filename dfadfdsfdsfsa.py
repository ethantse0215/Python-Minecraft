# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:01:31 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
time.sleep(2)
mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,161)
time.sleep(2)
mc.setBlocks(x,y,z,x,y+4,z,17)