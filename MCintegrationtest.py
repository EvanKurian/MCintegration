#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 18:21:02 2023

@author: evankurian
"""

import integrationpackage as ip
import numpy as np

def f(x):
    return 0.5*x**3



a=0 
b = 1
n = 500000

integral = ip.MCint(f, a, b, n)

print(f'integral = {integral: 0.3f}')
print("actual ans = 0.125")