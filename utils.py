import time

def read_input():
    n, budget = input().split()
    w = list(map(int,input().split()))
    v = list(map(int,input().split()))

    return int(n), int(budget), w, v