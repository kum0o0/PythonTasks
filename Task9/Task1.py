import numpy as np

matrix = np.loadtxt('task1.txt', delimiter=',')

print("Summ of elements:",np.sum(matrix))
print("Max element:",np.max(matrix))
print("Min element:",np.min(matrix))