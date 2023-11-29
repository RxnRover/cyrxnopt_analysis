import unittest

from cyrxnopt_analysis.SQSnobFitResultsStrategy import SQSnobFitResultsStrategy


class TestSQSnobFitResultsStrategy(unittest.TestCase):
    def test_analyze_results(self):
        results_file = "tests/example_results/sqsnobfit_results.json"

        corr_best_coords = [-0.51648, -0.5157200000000001]
        corr_best_value = 34.03973630433836
        corr_best_iter = 25
        corr_total_iter = 81
        corr_message = "N/A"

        strat = SQSnobFitResultsStrategy()

        results = strat.analyze_results(results_file)

        self.assertListEqual(results.best_coords, corr_best_coords)
        self.assertAlmostEqual(results.best_value, corr_best_value)
        self.assertEqual(results.best_iter, corr_best_iter)
        self.assertEqual(results.total_iter, corr_total_iter)
        self.assertEqual(results.message, corr_message)
