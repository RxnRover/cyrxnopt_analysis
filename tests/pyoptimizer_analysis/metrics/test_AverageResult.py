import unittest

from pyoptimizer_analysis.metrics.AverageResult import AverageResult
from pyoptimizer_analysis.OptimizerResult import OptimizerResult


class TestAverageResult(unittest.TestCase):
    def test_averaging_results(self):
        result = OptimizerResult()
        result.best_value = 2

        result2 = OptimizerResult()
        result2.best_value = 3

        result3 = OptimizerResult()
        result3.best_value = 4

        results = [result, result2, result3]

        metric = AverageResult()
        metric.calculate(results)

        self.assertAlmostEqual(3, metric.result)
        self.assertAlmostEqual(3, metric.average_value)
        self.assertEqual(3, metric.total_cycles)
        self.assertEqual(9, metric.total_value)

    def test_averaging_no_results(self):
        results = []

        metric = AverageResult()
        metric.calculate(results)

        self.assertAlmostEqual(0, metric.result)
        self.assertAlmostEqual(0, metric.average_value)
        self.assertEqual(0, metric.total_cycles)
        self.assertEqual(0, metric.total_value)
