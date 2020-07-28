# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:42:19 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z,19)
    time.sleep(0.01)
