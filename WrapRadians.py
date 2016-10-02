import numpy as np

def zeroto2pi(radians):
    return radians - 2*np.pi*np.floor(radians/(2*np.pi))

def pitopi(radians):
    return radians - 2*np.pi*np.floor((radians+np.pi)/(2*np.pi))

def zerotopi(radians):
    return radians - np.pi*np.floor(radians/(np.pi))