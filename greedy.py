# Greedy
from time import time

from utils import read_input

def greedy_solve(n, budget, w, v):
    # Sort item by v_i/w_i, descending
    items = [( i, v[i] * 1.0 / w[i]) for i in range(n)]
    items.sort(key= lambda item : item[1], reverse=True)

    value = 0
    for item in items:
        idx, _ = item
        if budget <= w[idx]:
            break

        value += v[idx]
        budget -= w[idx]

    return value

if __name__ == "__main__":

    n, budget, w, v = read_input()
    start_time = time()
    print(greedy_solve(n, budget, w, v))
    print(time() - start_time)
