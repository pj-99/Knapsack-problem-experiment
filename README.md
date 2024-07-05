# Knapsack probelem expirments

This repo contains different algos for solving knapsack problem.
And it also contains an experiment, which is mainly about how rounding algo with differenct epslions can affect the time and performance.

- For NCCU advanced algorithm course

- The following test is used to check the correctness of used algos
  - https://cses.fi/problemset/task/1158/


## Testcases generation
Since this project aim to examine the rounding algo which **round the item value**


Original DP time complexisty:
- $O(nB)$, where $B$ is the budget

Rounding DP time complexity:
- $O(\frac{1}{\epsilon} n^3)$

To show rounding DB faster, B should bigger than ( $n^3*\frac{1}{\epsilon}$ )

- 選擇該隨機分佈的理由？
- The random function use **normal distribution**. Since consider the real world problem like knapsack problem, it is mainly about resource allocations, which is tend to be normal distribution.

### Testcase input format

As same as [CSES Problem Set - Book Shop](https://cses.fi/problemset/task/1158/) input foramt. Each input has three lines:
```python
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


## How to run
1. Run all algos using input file inside `tests` folder
```sh
python run_exp.py
```

2. After completed, the result will be generated in `tests` folder

3. Show the result comparision
```sh
python show_exp_result.py
```

#### Verfiy correctness

```sh
python run_verify.py
```
This will compare all algo's acutal output with expected output


## Note
1. 使用 CSES 的測資，驗證演算法準確性，feasibility
2. 跑測試，扣掉 IO 時間，將資料彙整於 CSV
3. 畫圖

# Remove test run results file
```sh
# Remove file in tests_exp whose file name is ending with 2358
./remove_test_files.sh ./tests_exp 2358
```

## Compared algos
1. Original DP  `dp.py` : as ground truth for validating result
2. Fractional knapsack `fractional.py`  : as upper bound (fast😄)
3. Greedy `greedy`: as the fast approach
4. Modified `modified_greedy` : as the fast approach and better than greedy
   - it is greedy, but consider the pickable max-value item
