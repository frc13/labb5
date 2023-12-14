import numpy as np

def f(x):
    return x - np.tan(x)

def iterasyon_yontemi(f, x0, epsilon, max_iter):
    iterasyon_sayisi = 0
    while True:
        x1 = np.tan(x0)
        iterasyon_sayisi += 1
        if np.abs(x1 - x0) < epsilon or iterasyon_sayisi >= max_iter:
            break
        x0 = x1
    return x1, iterasyon_sayisi

x0 = 1.0
epsilon = 1e-2
max_iter = 100

root, iterations = iterasyon_yontemi(f, x0, epsilon, max_iter)
print("Kök:", root)
print("İterasyon Sayısı:", iterations)
