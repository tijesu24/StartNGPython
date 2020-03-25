# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:09:34 2020

@author: Tijesunimi.Adebiyi
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 14:30:17 2020

@author: Tijesunimi.Adebiyi
"""

import math

while(True):
    radius = input('Input the circle radius: ')
    try:
        radius = float(radius)
    except(ValueError): #if we can't cast to float
        print('Please enter a number!')
        continue
    
    area = math.pi * radius**2
    print('Area:',area)
    
    break