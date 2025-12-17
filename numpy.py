# Numpy Calculation
import numpy as np

numbers = list(map(float, input("Enter numbers separated by space: ").split()))

arr = np.array(numbers)

mean = np.mean(arr)
median = np.median(arr)

print("Mean =", mean)
print("Median =", median)
