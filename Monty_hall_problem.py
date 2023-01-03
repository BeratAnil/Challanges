import numpy as np
import random

true_array = np.array([])
liste = []
array = np.array([True, False, False])


def run(n):
    for i in range(n):
        secim = random.choice(array)

        if secim == True:
            liste.append(1)
        else:
            liste.append(2)
    return (liste)


a = run(10000)

b = a.count(2) / 10000

print(b)