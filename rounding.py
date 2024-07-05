from time import time
from utils import read_input
import argparse
from math import ceil, inf

# TODO: Check if other algo need to use loop instead of recursion like this one
def dp_exactly_val_solve(n, budget, w, vals):
    total_v = sum(vals)

    # Init dp[i][v]
    dp = [[inf] * (total_v + 1) for _ in range(n)]
    dp[0][0] = 0
    dp[0][vals[0]] = w[0]

    for i in (range(1, n)):
        for v in range(1, total_v+1):
            dp[i][v] = dp[i-1][v] # don't pick current

            if v >= vals[i]: # Otherwise < 0
                dp[i][v] = min(
                    dp[i][v],
                    dp[i-1][v-vals[i]] + w[i] # pick current
                )

    max_val = 0
    for v in range(total_v, -1, -1): # Start from the larger v
        if dp[n-1][v] <= budget:
            max_val = v
            break

    return max_val

def rounding(epsilon, lowerbound, n, v, w):
    # Do rounding
    x = (epsilon * lowerbound) / n
    # Note! Make sure x is greater than 1
    if(x <= 1):
        return v, w

    # If value[i] after rounding = 0, remove it
    new_v = []
    new_w = []
    for i in range(n):
        new_v_i = ceil(v[i]/x)
        if new_v_i > 0:
            new_v.append(new_v_i)
            # print(f"old vi: {v[i]} / new vi: {new_v_i}")s
            new_w.append(w[i])

    return new_v, new_w

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("e", help="eplison", type=float, default=0)
    args = parser.parse_args()

    epsilon = args.e

    n, budget, w, v = read_input()

    start_time = time()

    # Rounding vals
    if epsilon > 0:
        lowerbound = max(v)
        v, w = rounding(epsilon, lowerbound, n, v, w)

    print(dp_exactly_val_solve(n, budget, w, v))

    print(time() - start_time)
