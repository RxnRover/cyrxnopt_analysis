import os
import unittest

from cyrxnopt_analysis.utilities.get_files import get_files


class TestGetFiles(unittest.TestCase):
    def test_get_files_top_dir(self):
        results_directory = os.path.join("tests", "example_results")
        results_pattern = r"[a-zA-z0-9]+_test.tmp"

        corr_file_list = [
            os.path.join("tests", "example_results", "config_test.tmp")
        ]

        file_list = get_files(results_directory, results_pattern)

        self.assertListEqual(file_list, corr_file_list)

    def test_get_files_recusively(self):
        results_directory = "tests"
        results_pattern = r"[a-zA-z0-9]+_test.tmp"

        corr_file_list = [
            os.path.join("tests", "example_results", "config_test.tmp")
        ]

        file_list = get_files(
            results_directory, results_pattern, recursive=True
        )

        self.assertListEqual(file_list, corr_file_list)
