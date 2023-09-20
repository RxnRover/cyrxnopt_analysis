import json
import pandas as pd

from pyoptimizer_analysis.OptimizerResult import OptimizerResult
from pyoptimizer_analysis.ReadResultsStrategy import ReadResultsStrategy


class SQSnobFitResultsStrategy(ReadResultsStrategy):
    def analyze_results(self, result_file: str) -> OptimizerResult:
        """Analyzes results from the SQSnobFit optimizer.

        :param result_file: File to read the results from. This must be
                            formatted as a JSON file.
        :type result_file: str

        :return: Aggregated results from the optimization.
        :rtype: Results
        """

        with open(result_file, "r") as fin:
            sqsnobfit_results = json.load(fin)

        results = OptimizerResult()

        df = pd.DataFrame(sqsnobfit_results["raw_results"])
        df['yield'] = df.pop(0)


        results.best_coords = sqsnobfit_results["best_coords"]
        results.best_value = sqsnobfit_results["best_value"]
        results.best_iter = sqsnobfit_results["best_iter"]
        results.total_iter = sqsnobfit_results["total_iter"]
        results.message = sqsnobfit_results["message"]
        results.raw_results = df

        return results
