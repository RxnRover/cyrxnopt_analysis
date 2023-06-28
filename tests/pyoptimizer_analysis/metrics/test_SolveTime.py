import unittest

from pyoptimizer_analysis.metrics.SolveTime import SolveTime
from pyoptimizer_analysis.OptimizerResult import OptimizerResult


class TestSolveTime(unittest.TestCase):
    def test_map_invalid_valid_mixed_results(self):
        # Successful optimization
        result = OptimizerResult()
        result["function"] = "branin"
        result.best_value = 0.39789
        result.best_iter = 40

        # Successful optimization
        result2 = OptimizerResult()
        result2["function"] = "branin"
        result2.best_value = 0.4
        result2.best_iter = 50

        # Not successful optimization
        result3 = OptimizerResult()
        result3["function"] = "branin"
        result3.best_value = 1000
        result3.best_iter = 100

        results = [result, result2, result3]

        metric = SolveTime(0.39788735772973816)
        metric.calculate(results)

        self.assertEqual(45, metric.result)

    def test_map_no_valid_results(self):
        result = OptimizerResult()
        result["function"] = "branin"
        result.best_value = 10000
        result.best_iter = 40

        result2 = OptimizerResult()
        result2["function"] = "branin"
        result2.best_value = 60
        result2.best_iter = 50

        results = [result, result2]

        metric = SolveTime(0.39788735772973816)
        metric.calculate(results)

        self.assertEqual(0, metric.result)

    def test_map_optimum_zero(self):
        # Successful optimization
        result = OptimizerResult()
        result["function"] = "zero"
        result.best_value = 0.0001
        result.best_iter = 40

        # Not successful optimization
        result2 = OptimizerResult()
        result2["function"] = "zero"
        result2.best_value = 1000
        result2.best_iter = 100

        results = [result, result2]

        metric = SolveTime(0)
        metric.calculate(results)

        self.assertEqual(40, metric.result)
