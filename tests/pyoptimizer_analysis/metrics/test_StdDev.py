import unittest

from pyoptimizer_analysis.metrics.StdDev import StdDev
from pyoptimizer_analysis.OptimizerResult import OptimizerResult


class TestStdDev(unittest.TestCase):
    def test_stddev_results(self):
        result = OptimizerResult()
        result.best_value = 2

        result2 = OptimizerResult()
        result2.best_value = 3

        result3 = OptimizerResult()
        result3.best_value = 4

        results = [result, result2, result3]

        metric = StdDev()
        metric.calculate(results)

        self.assertAlmostEqual(1, metric.result)
        self.assertAlmostEqual(1, metric.stddev)
        self.assertEqual(3, metric.total_cycles)
        self.assertEqual([2, 3, 4], metric.sample_set)

    def test_stddev_no_results(self):
        results = []

        metric = StdDev()
        metric.calculate(results)

        self.assertAlmostEqual(0, metric.result)
        self.assertAlmostEqual(0, metric.stddev)
        self.assertEqual(0, metric.total_cycles)
        self.assertEqual([], metric.sample_set)
