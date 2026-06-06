import numpy as np
def ramanujan_generator(n=10):
    return np.exp(np.pi * np.sqrt(np.arange(1, n+1)))
