# Original dynamic programming algo
import sys
from functools import lru_cache
from time import time

from utils import read_input

sys.setrecursionlimit(1000000)

def dp_solve(n, budget, w, v):
    @lru_cache(maxsize=None)
    def k(i, b):
        """
        Return max values within b and 0~i items
        """

        if i == 0:
            return v[i] if w[i] <= b else 0

        if w[i] > b: # Cannot pick
            return k(i-1, b)

        return max(
            k(i-1, b), # Don't pick current item
            k(i-1, b-w[i])+v[i] # Pick
        )
    return k(n-1, budget)

if __name__ == "__main__":

    n, budget, w, v = read_input()
    start_time = time()
    print(dp_solve(n, budget, w, v))
    print(time() - start_time)
