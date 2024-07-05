# Greedy
from time import time

from utils import read_input

def greedy_solve(n, budget, w, v):

    # Find the item_i has the highest value within budget
    max_value_item = 0 # within budget
    for i in range(n):
        if w[i] <= budget:
            max_value_item = max(max_value_item, v[i])

    # Calculate greedy
    items = [( i, v[i] * 1.0 / w[i]) for i in range(n)]
    items.sort(key= lambda item : item[1], reverse=True)

    greedy_value = 0
    for item in items:
        idx, _ = item
        if budget <= w[idx]:
            break

        greedy_value += v[idx]
        budget -= w[idx]

    return max(max_value_item, greedy_value)

if __name__ == "__main__":

    n, budget, w, v = read_input()
    start_time = time()
    print(greedy_solve(n, budget, w, v))
    print(time() - start_time)
