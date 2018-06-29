# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 13:30:57 2018

@author: JPBDell
"""
import math
import numpy as np
import matplotlib

roughnesses = [.05, .04, .3, .02, .015, .01, .005, .002, .001, 5e-4, 2e-4, 1e-4, 5e-5, 10e-5, 5e-6, 10e-6]

def approx_colebrook(reynolds, rel_roughness):
    f = (1/(-1.8*math.log((6.9/reynolds +(rel_roughness/3.7)**1.11),10)))**2
    return f
    
def lam_f(reynolds, rel_roughness):
    f = 64/reynolds
    return f

def fully_turb(reynolds, rel_roughness):
    return [if(reynolds>3500/rel_roughness) approx_colebrook(reynolds, rel_roughness)]

def implicit_colebrook(reynolds, rel_roughness, f):
    return f**-0.5 + 2*math.log(rel_roughness/3.7+2.51/reynolds*f**-0.5,10)