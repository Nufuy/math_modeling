import matplotlib.pyplot as plt
import numpy as np

def kk(k, fi):
    x = k/np.sqrt(fi) * np.sin(fi)
    y = k/np.sqrt(fi) * np.cos(fi)