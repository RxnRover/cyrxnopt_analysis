import unittest

from cyrxnopt_analysis.EDBOpResultsStrategy import EDBOpResultsStrategy


class TestEDBOpResultsStrategy(unittest.TestCase):
    def test_analyze_results(self):
        results_file = "tests/example_results/edbop/my_optimization_edbop.csv"

        corr_best_coords = [9.799998999999946, 2.0]
        corr_best_value = 1.7215444334809558
        corr_best_iter = 20
        corr_total_iter = 100

        strat = EDBOpResultsStrategy()

        results = strat.analyze_results(results_file)

        self.assertListEqual(results.best_coords, corr_best_coords)
        self.assertAlmostEqual(results.best_value, corr_best_value)
        self.assertEqual(results.best_iter, corr_best_iter)
        self.assertEqual(results.total_iter, corr_total_iter)
