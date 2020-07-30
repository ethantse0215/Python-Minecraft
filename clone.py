# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:08:50 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
x,y,z = mc.player.getTilePos
number = 1
for i in range (8):
    for j in range(number):
        mc.spawnEntity(x,y,z,20)
    number = number*2
    mc.postTpChat("spawned"+str(number)+"tnts")