import unittest

from cyrxnopt_analysis.OptimizerResult import OptimizerResult
from cyrxnopt_analysis.transforms.GetFunctionName import GetFunctionName


class TestGetFunctionName(unittest.TestCase):
    def test_map_function_name(self):
        results_file = "file/path/branin_0/results.json"

        result = OptimizerResult()
        result.filename = results_file

        results = GetFunctionName.map([result])

        self.assertEqual(results[0]["function"], "branin")

    def test_map_invalid_directory_name(self):
        results_file = "file/path/branin/results.json"

        result = OptimizerResult()
        result.filename = results_file

        self.assertRaises(RuntimeError, GetFunctionName.map, [result])
