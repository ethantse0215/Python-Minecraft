# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:41:22 2020

@author: appedu
"""
print("Minecraft")  
import time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

print()
print(mc.player.getTilePos())

"""ayer.setTilePos(-245,64,243)
time.sleep(10)"""

x=-245
y=64
z=243

mc.player.setTilePos(x,y,z)
