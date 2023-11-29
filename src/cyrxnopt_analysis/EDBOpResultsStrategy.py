import json
import os

import pandas as pd

from cyrxnopt_analysis.OptimizerResult import OptimizerResult
from cyrxnopt_analysis.ReadResultsStrategy import ReadResultsStrategy


class EDBOpResultsStrategy(ReadResultsStrategy):
    def analyze_results(self, result_file: str) -> OptimizerResult:
        """Analyzes results from the EDBOP optimizer.

        :param result_file: File to read the results from. This must be
                            formatted as a JSON file.
        :type result_file: str

        :return: Aggregated results from the optimization.
        :rtype: Results
        """

        results = OptimizerResult()
        df = pd.read_csv(result_file)

        data = df[df["priority"] == -1]
        data = data.drop("priority", axis=1)
        data = data.reset_index(drop=True)
        data["yield"] = pd.to_numeric(data["yield"])

        # max_val = -data["yield"].max()
        # idmax = data["yield"].idxmax() + 1

        # best_conditions =
        # data.loc[data["yield"].idxmax()][:-1].values.tolist()

        tmp_results_file = os.path.dirname(result_file)
        tmp_results_file = os.path.join(tmp_results_file, "results.json")
        with open(tmp_results_file, "r") as fin:
            edbop_results = json.load(fin)

        results = OptimizerResult()

        results.best_coords = edbop_results["best_coords"]
        results.best_value = edbop_results["best_value"]
        results.best_iter = edbop_results["best_iter"]
        results.total_iter = edbop_results["total_iter"]
        results.message = edbop_results["message"]
        results.raw_results = edbop_results["raw_results"]

        return results
