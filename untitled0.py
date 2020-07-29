# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:30:34 2020

@author: appedu
"""


mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
while True:
    hits = mc.events.pollBlockhits()
    if len(hits)>0: 
         blockID = mc.getBlock(x,y,z)
         print("your hunting block ID is"+str(blockID)+"block")
         mc.postToChat("your hunting block ID is"+str(blockID)+"block")