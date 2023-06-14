import json

from pyoptimizer_analysis.ReadResultsStrategy import ReadResultsStrategy
from pyoptimizer_analysis.Results import Results


class SQSnobFitResultsStrategy(ReadResultsStrategy):
    def analyze_results(self, result_file: str) -> Results:
        """Analyzes results from the SQSnobFit optimizer.

        :param result_file: File to read the results from. This must be
                            formatted as a JSON file.
        :type result_file: str

        :return: Aggregated results from the optimization.
        :rtype: Results
        """

        with open(result_file, "r") as fin:
            sqsnobfit_results = json.load(fin)

        results = Results()

        results.best_coords = sqsnobfit_results["best_coords"]
        results.best_value = sqsnobfit_results["best_value"]
        results.best_iter = sqsnobfit_results["best_iter"]
        results.total_iter = sqsnobfit_results["total_iter"]
        results.message = sqsnobfit_results["message"]
        results.raw_results = sqsnobfit_results["raw_results"]

        return results
