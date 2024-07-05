''' Generate testcase

Format
```
n budget
w[0] w[1] w[2] ... w[n-1]
v[0] v[1] v[2] ... v[n-1]
```

Example:
```
4 10
4 8 5 3
5 12 8 1
```
'''
import random
import argparse
import matplotlib.pyplot as plt
import numpy as np

''' Generate testcase

Format
```
n budget
w[0] w[1] w[2] ... w[n-1]
v[0] v[1] v[2] ... v[n-1]
```

Example:
```
4 10
4 8 5 3
5 12 8 1
```
'''
import random
import argparse

def generate_testcase(output_file):
    budget = 1e6
    n = 100

    w = [random.randint(1, budget/10) for _ in range(n)]
    v = [random.randint(1, budget/10) for _ in range(n)]

    with open(output_file, 'w') as f:
        f.write(f"{n} {int(budget)}\n")
        f.write(" ".join(map(str, w)) + "\n")
        f.write(" ".join(map(str, v)) + "\n")

    # Show distribution of w and v
    # Show distribution of w and v
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.hist(w, bins=20, edgecolor='black')
    plt.title('Distribution of Weights (w)')
    plt.xlabel('Weight')
    plt.ylabel('Frequency')

    plt.subplot(1, 2, 2)
    plt.hist(v, bins=20, edgecolor='black')
    plt.title('Distribution of Values (v)')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.savefig(output_file.replace('.in', '_distribution.png'))
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", help="how many test case files should be generated", default=3, type=int)
    args = parser.parse_args()

    for i in range(1, args.n+1):
        generate_testcase(f"{i}_uni.in")
