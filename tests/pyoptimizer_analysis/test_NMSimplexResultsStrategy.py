import unittest

from pyoptimizer_analysis.NMSimplexResultsStrategy import NMSimplexResultsStrategy


class TestNMSimplexResultsStrategy(unittest.TestCase):
    def test_analyze_results(self):
        results_file = "tests/example_results/nmsimplex_results.json"

        corr_best_coords = [3.141592649445112, 2.2749999841912176]
        corr_best_value = 0.39788735772973816
        corr_best_iter = 88
        corr_total_iter = 88
        corr_message = "Optimization terminated successfully."
        corr_raw_results = "N/A"

        strat = NMSimplexResultsStrategy()

        results = strat.analyze_results(results_file)

        self.assertListEqual(results.best_coords, corr_best_coords)
        self.assertAlmostEqual(results.best_value, corr_best_value)
        self.assertEqual(results.best_iter, corr_best_iter)
        self.assertEqual(results.total_iter, corr_total_iter)
        self.assertEqual(results.message, corr_message)
        self.assertEqual(results.raw_results, corr_raw_results)
