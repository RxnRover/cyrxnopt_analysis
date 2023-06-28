import unittest

from pyoptimizer_analysis.metrics.SolveTime import SolveTime
from pyoptimizer_analysis.OptimizerResult import OptimizerResult


class TestGetFunctionName(unittest.TestCase):
    def test_map_function_name(self):
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
