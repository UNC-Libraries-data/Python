#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SOLUTION FOR FILES_PACKAGES EXERCISE
"""

for fname in flist:    
    
    with open(fname,"r") as txtfile:
        recipe=txtfile.read()
        
    for s in seasons:
        for ingredient in seasons[s]:           
             if (ingredient in recipe.lower()):  #.lower() changes all text in the recipe to lowercase
                shutil.copyfile(fname, os.path.join(s, fname)) #os.path.join() joins the folder name with the file name