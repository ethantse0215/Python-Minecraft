# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:59:19 2020

@author: appedu
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
t=5
while t<10:
    mc.postToChat("hello")
    t=t+1 