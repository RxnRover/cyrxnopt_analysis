import json

from pyoptimizer_analysis.OptimizerResult import OptimizerResult
from pyoptimizer_analysis.ReadResultsStrategy import ReadResultsStrategy


class NMSimplexResultsStrategy(ReadResultsStrategy):
    def analyze_results(self, result_file: str) -> OptimizerResult:
        """Analyzes results from the Nelder-Mead optimizer.

        :param result_file: File to read the results from. This must be
                            formatted as a JSON file.
        :type result_file: str

        :return: Aggregated results from the optimization.
        :rtype: Results
        """

        with open(result_file, "r") as fin:
            nmsimplex_results = json.load(fin)

        results = OptimizerResult()

        results.best_coords = nmsimplex_results["best_coords"]
        results.best_value = nmsimplex_results["best_value"]
        results.best_iter = nmsimplex_results["best_iter"]
        results.total_iter = nmsimplex_results["total_iter"]
        results.message = nmsimplex_results["message"]
        results.raw_results = nmsimplex_results["raw_results"]

        return results
