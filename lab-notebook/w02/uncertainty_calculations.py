# Goal: Using week 1's data, I will derive the standard error of the mean and check it numerically against my week 1 results

import numpy as np

data = np.array([997, 1003, 995, 1001, 1006, 998, 1004, 992, 999, 1007, 996, 1002, 994, 1000, 1005, 997, 1008, 993, 1001, 999])
mean = np.mean(data)
s = np.std(data, ddof=1)

numpy_result = s / np.sqrt(20)
print(f"Mean = {mean:.2f} Ohms")
print(f"Sample standard deviation (s) = {s:.2f} Ohms")

print("\nBy hand:")
print(f"s / sqrt(20) = {s:.2f} / sqrt(20)")
print(f"         = {s / np.sqrt(20):.4f} Ohms")

print("\nUsing NumPy:")
print(f"s / np.sqrt(20) = {numpy_result:.4f} Ohms")

print("\nMatch Result")
print(np.isclose(s / np.sqrt(20), numpy_result))
