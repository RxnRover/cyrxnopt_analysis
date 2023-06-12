import unittest

from pyoptimizer_analysis.AMLROResultsStrategy import AMLROResultsStrategy


class TestAMLROResultsStrategy(unittest.TestCase):
    def test_analyze_results(self):
        results_file = "tests/example_results/training_set_file_amlro.txt"

        corr_best_coords = [9.3, 1.9]
        corr_best_value = 0.6950967297896149
        corr_best_iter = 2
        corr_total_iter = 100

        strat = AMLROResultsStrategy()

        results = strat.analyze_results(results_file)

        self.assertListEqual(results.best_coords, corr_best_coords)
        self.assertAlmostEqual(results.best_value, corr_best_value)
        self.assertEqual(results.best_iter, corr_best_iter)
        self.assertEqual(results.total_iter, corr_total_iter)
