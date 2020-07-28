# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:18:33 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z = mc.player.getTilePos()
mc.setBlocks(x,y,z,x+10,y+10,z+10,57)
mc.setBlocks(x+1,y+1,z+1,x+9,y-9,z+9,0)