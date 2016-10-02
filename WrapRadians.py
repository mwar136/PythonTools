import numpy as np

def wrapto2pi(radians):
    return radians - 2*np.pi*np.floor(radians/(2*np.pi))

def wraptopi(radians):
    return radians - np.pi*np.floor(radians/(np.pi))