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
             if (ingredient in recipe.lower()):
                shutil.copyfile(fname, os.path.join(s, fname))
