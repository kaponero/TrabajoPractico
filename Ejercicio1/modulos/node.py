# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:39:21 2022

@author: kapon
"""

class Node:
    def __init__(self,data):
        self.item = data
        self.nref = None
        self.pref = None