import numpy as np

def approach_napier(n):
    return (1 + 1/n)**n

n_list = [2, 4, 10, 100, 1000, 10000, 100000]
for n in n_list:
    print("a_"+ str(n) + " =", approach_napier(n))
