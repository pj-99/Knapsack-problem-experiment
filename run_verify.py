# Read tests from tests folder
# input: 1.in, 2.in, 3.in, 4.in, 5.in ...
# output: 1.out, 2.out, 3.out, 4.out, 5.out ...

import os
import unittest
import time
from enum import Enum
class AssertComparator(Enum):
    EQUAL=1 # Expected == Acutal
    GREATER_EQUAL=2 # Expected >= Actural
    LESS_EQUAL=3 # Expected <= Actual

class TestAlgo(unittest.TestCase):

    def test_dp(self):
        self.run_rest("dp.py", AssertComparator.EQUAL)

    def test_rounding_0_5(self):
        self.run_rest("rounding.py", AssertComparator.GREATER_EQUAL, extra_args="0.5")

    # def test_rounding_0_1(self):
    #     self.run_rest("rounding.py", AssertComparator.GREATER_EQUAL, extra_args="0.1")

    def test_modified_greedy(self):
        self.run_rest("modifiedgreedy.py", AssertComparator.GREATER_EQUAL)

    def test_greedy(self):
        self.run_rest("greedy.py", AssertComparator.GREATER_EQUAL)

    def test_fractional(self):
        self.run_rest("fractional.py", AssertComparator.LESS_EQUAL)

    def run_rest(self, algo_file, assertComp: AssertComparator, extra_args = ""):
        # For output naming
        algo = algo_file.split(".")[0] + extra_args.replace(".", "_")
        postfix = time.strftime("%H%M")

        folder = "tests_correct"
        files = os.listdir(folder)
        input_files = [f for f in files if f.endswith(".in")]
        input_files.sort(key=lambda x: (x.split(".")[0]))
        for i, f in enumerate(input_files):
            with self.subTest(i=i):
                # Get input file name
                input_file = f
                # Get output file name
                output_file = f.replace(".in", ".out_alg_"+ algo + f"_{postfix}")
                expect_output_file = f.replace(".in", ".out")
                print("------")
                print("Testcase", f)
                # Run algo to generate output
                os.system(f"python3 {algo_file} {extra_args} < {folder}/" + input_file + f" > {folder}/" + output_file)

                # Compare alg output with expected output
                with open(f"{folder}/" + output_file, "r") as fp:
                    alg_output = int_or_float(fp.readline())
                with open(f"{folder}/" + expect_output_file, "r") as fp:
                    expect_output = int_or_float(fp.readline())
                print("ALG:", alg_output, ", OPT:", expect_output)
                if assertComp == AssertComparator.EQUAL:
                    self.assertTrue(expect_output == alg_output, f"Expected: {expect_output}, Actual: {alg_output}")
                elif assertComp == AssertComparator.GREATER_EQUAL:
                    self.assertTrue(expect_output >= alg_output, f"Expected: {expect_output}, Actual: {alg_output}")
                elif assertComp == AssertComparator.LESS_EQUAL:
                    self.assertTrue(expect_output <= alg_output, f"Expected: {expect_output}, Actual: {alg_output}")


def int_or_float(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

if __name__ == '__main__':
    unittest.main()