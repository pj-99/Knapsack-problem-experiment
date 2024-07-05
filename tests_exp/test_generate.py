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
    budget =  1e6
    n = 100

    mu = 1.5e5  # 150000
    sigma = 2.5e4  # 25000

    w = [random.normalvariate(mu, sigma) for _ in range(n)]
    v = [random.normalvariate(mu, sigma) for _ in range(n)]

    # Prevent negative
    w = [max(1, int(x)) for x in w]
    v = [max(1, int(x)) for x in v]

    with open(output_file, 'w') as f:
        f.write(f"{int(n)} {int(budget)}\n")
        f.write(" ".join(map(str, w))+ "\n")
        f.write(" ".join(map(str, v)) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", help="how many test case files should be generated", default=2)
    args = parser.parse_args()

    for i in range(1, args.n+1):
        generate_testcase(f"{i}.in")
