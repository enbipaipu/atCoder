import numpy as np

N = int(input())

out = np.base_repr(N - 1, 5)

print(2 * int(out))
