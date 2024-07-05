# Knapsack probelem expirments

This repo contains different algorthims for knapsack problem and an experiment process to collect outputs and plot the results.

- For NCCU advanced algorithm course
- The following test is used to check the correctness of used algos
  - https://cses.fi/problemset/task/1158/

## Algorthims
- Dynamic progamming: `dp.py`
- Rounding values of item using DP: `rounding.py`
- Greedy: `greedy.py` and `modifiedgreedy.py`
- fractional(UB): `fractional.py`

## Run experiment

1. Run all algos using input file inside `tests_exp` folder, the result will be generated in the same folder.
```sh
python run_exp.py
```

2. Create a csv containing all the results.
```sh
python create_exp_result.py
```

3. Plot the results.
```sh
python plot_result.py
```

----

## Verfiy correctness of algos

```sh
python run_verify.py
```
### Remove test output files
```sh
./remove_test_files.sh $folder $postfix $postfix_2? $postfix_3?
# Remove file in tests_exp whose file name is ending with 2358 or 2359
./remove_test_files.sh ./tests_exp 2358
```

