# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:00:41 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import random,time
mc = Minecraft.create()
pos = mc.player.getTilePos()
while True:
    x = pos.x + random.uniform(-20,20)
    y = pos.y +30
    z = pos.z + random.uniform(-20,20)
    mc.spawnEntity(x,y,z,45)
    time.sleep(0.1)
    