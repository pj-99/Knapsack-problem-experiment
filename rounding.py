from time import time
from utils import read_input
import argparse
from math import ceil, inf
import modifiedgreedy
from tqdm import tqdm

def dp_exactly_val_solve(n, budget, w, vals, old_vals):
    total_v = sum(vals)
    # print(f"Total value: {total_v}")

    # Originall, init dp[i][v] = [min budget, resotred result value(before rounding)]
    # But for saving space, we can store only the current row
    # dp[v] = [min budget, resotred result value(before rounding)]
    dp = [(inf, 0)] * (total_v + 1)
    dp[0] = (0, 0)
    dp[vals[0]] = (w[0], old_vals[0])

    for i in tqdm(range(1, n)):
        prev_dp = dp[:]
        for v in tqdm(range(1, total_v+1)):
            skip_budget, skip_old_val = prev_dp[v]

            # dp[i][v] = (
            #     min(skip_budget, pick_budget),
            #     skip_old_val if skip_budget < pick_budget else pick_old_val
            # )

            if v >= vals[i]:
                prev_budget, prev_old_val = prev_dp[v-vals[i]]
                pick_budget = prev_budget + w[i]
                pick_old_val = prev_old_val + old_vals[i]
                if pick_budget < skip_budget:
                    dp[v] = (pick_budget, pick_old_val)
                else:
                    dp[v] = (skip_budget, skip_old_val)
            else:
                dp[v] = (skip_budget, skip_old_val)


    max_old_val = 0
    for v in range(total_v, -1, -1): # Start from the larger v
        if dp[v][0] <= budget:
            _, max_old_val = dp[v]
            break

    return max_old_val

def calc_rounding_amount(epsilon, lowerbound, n):
    return (epsilon * lowerbound) / n

def rounding(x, n, v, w):
    # Note! Make sure x is greater than 1
    if(x <= 1):
        raise ValueError("x must be greater than 1")

    # If value[i] after rounding = 0, remove it
    new_v = []
    for i in range(n):
        new_v_i = ceil(v[i]/(x*1.0))
        new_v.append(new_v_i)

    return new_v, w

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("e", help="eplison", type=float, default=0)
    args = parser.parse_args()

    epsilon = args.e

    n, budget, w, v = read_input()

    start_time = time()

    # Rounding vals
    if epsilon > 0:
        lowerbound = modifiedgreedy.greedy_solve(n, budget, w, v)

        x = calc_rounding_amount(epsilon, lowerbound, n)
        old_v = v
        if x >= 1:
            v, w = rounding(x, n, v, w)

        # print(f"Epsilon {epsilon}, Rounding amount x: {x}")
        real_val_sum = dp_exactly_val_solve(n, budget, w, v, old_v)
        print(real_val_sum)
    else:
        real_val_sum = dp_exactly_val_solve(n, budget, w, v, v)
        print(real_val_sum)
    print(time() - start_time)
