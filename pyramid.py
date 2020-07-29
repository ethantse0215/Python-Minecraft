# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:08:32 2020

@author: appedu
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

for i in range (100):
    mc.setBlocks(x-i,y-i,z-i,x+i,y-i,z+i,7)
   

