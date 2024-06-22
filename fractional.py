# Fracional
from time import time

from utils import read_input

def fractional_solve(n, budget, w, v):
    # Sort item by v_i/w_i, descending
    items = [( i, v[i] * 1.0 / w[i]) for i in range(n)]
    items.sort(key= lambda item : item[1], reverse=True)

    value = 0.0
    for item in items:
        if budget <= 0:
            break
        idx, cp_ratio = item
        cost = min(w[idx], budget) # Cost in this round
        value += (cost * cp_ratio)
        budget -= cost

    return value

if __name__ == "__main__":

    n, budget, w, v = read_input()
    start_time = time()
    print(fractional_solve(n, budget, w, v))
    print(time() - start_time)
