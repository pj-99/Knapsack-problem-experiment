# Read tests from tests folder
# input: 1.in, 2.in, 3.in, 4.in, 5.in ...
# output: 1.out, 2.out, 3.out, 4.out, 5.out ...

import os
import unittest
import numpy as np


TEST_FOLDER = "tests_exp"

class TestAlgo(unittest.TestCase):

    def test_dp(self):
        self.run_rest("dp.py")


    def test_rounding(self):

        for epsilon in np.arange(0.05, 0.6, 0.05):
            with self.subTest(epsilon=epsilon):
                epsilon = round(epsilon, 2)
                self.run_rest("rounding.py", extra_args=f"{epsilon}")

        # Extra test
        with self.subTest(epsilon=0.01):
            self.run_rest("rounding.py", extra_args="0.01")

        with self.subTest(epsilon=0.001):
            self.run_rest("rounding.py", extra_args="0.001")


    def test_modified_greedy(self):
        self.run_rest("modifiedgreedy.py")

    def test_greedy(self):
        self.run_rest("greedy.py")

    def test_fractional(self):
        self.run_rest("fractional.py")

    def run_rest(self, algo_file, extra_args = ""):
        # For output naming
        algo = algo_file.split(".")[0] + extra_args
        # postfix = time.strftime("%H%M")
        postfix="run1"

        files = os.listdir(TEST_FOLDER)
        input_files = [f for f in files if f.endswith(".in")]
        input_files.sort(key=lambda x: (x.split(".")[0]))
        for i, f in enumerate(input_files):
            with self.subTest(i=i):
                # Get input file name
                input_file = f
                # Get output file name
                output_file = f.replace(".in", ".out_alg_"+ algo + f"_{postfix}")
                print("------")
                print("Testcase", f)
                # Run algo to generate output
                os.system(f"python3 {algo_file} {extra_args} < {TEST_FOLDER}/" + input_file + f" > {TEST_FOLDER}/" + output_file)

                # Shoe expected output
                with open(f"{TEST_FOLDER}/" + output_file, "r") as fp:
                    alg_output = int_or_float(fp.readline())
                print("ALG:", alg_output)


def int_or_float(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

if __name__ == '__main__':
    unittest.main()