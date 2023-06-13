import unittest

from pyoptimizer_analysis.utilities.get_files import get_files


class TestGetFiles(unittest.TestCase):
    def test_get_files_top_dir(self):
        results_directory = "tests/example_results"
        results_pattern = r"[a-zA-z0-9]+_results.json"

        corr_file_list = ["tests/example_results/nmsimplex_results.json"]

        file_list = get_files(results_directory, results_pattern)

        self.assertListEqual(file_list, corr_file_list)

    def test_get_files_recusively(self):
        results_directory = "tests"
        results_pattern = r"[a-zA-z0-9]+_results.json"

        corr_file_list = ["tests/example_results/nmsimplex_results.json"]

        file_list = get_files(
            results_directory, results_pattern, recursive=True
        )

        self.assertListEqual(file_list, corr_file_list)
