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

        results = [result, result2]

        metric = SolveTime()
        metric.calculate(results)

        self.assertEqual(45, metric.solve_time)
        self.assertEqual(45, metric.result)
        self.assertEqual(2, metric.total_cycles)
        self.assertEqual(90, metric.total_iterations)
