# Knapsack problem expirments

- This repository contains various algorithms for the knapsack problem and an experiment process to collect outputs and plot the results.

- NCCU advanced algorithms course
- The following test is used to verify the correctness of the algorithms: https://cses.fi/problemset/task/1158/


## Algorithms
- Dynamic programming: `dp.py`
- Rounding values of item using DP: `rounding.py`
- Greedy: `greedy.py` and `modifiedgreedy.py`
- fractional(UB): `fractional.py`

## Run Experiment
- Steps 1 and 2 can be skipped if you only want to view the plot of the existing results in this repository.

1. Run all algorithms using the input file inside `tests_exp` folder. The results will be generated in the same folder.
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

## Verify Correctness of Algorithms

```sh
python run_verify.py
```


**Note: Remove test output files**
```sh
./remove_test_files.sh $folder $postfix $postfix_2? $postfix_3?...

# Example:
# Remove file in tests_exp whose file name is ending with 2358 or 2359
./remove_test_files.sh ./tests_exp 2358
```

