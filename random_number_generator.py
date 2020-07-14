#%% random_number_generator.py
import numpy as np

def generate_random_number(max = 1, min = 0, dec = 1):
    power = 1/dec
    interim_min = min*power
    interim_max = max*power
    interim_rand = np.random.randint(low = interim_min, high = interim_max, size = 1)
    rand = interim_rand/power
    return rand


# %%
