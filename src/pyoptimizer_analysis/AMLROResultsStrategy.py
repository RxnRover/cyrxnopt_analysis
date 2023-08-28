import pandas as pd

from pyoptimizer_analysis.OptimizerResult import OptimizerResult
from pyoptimizer_analysis.ReadResultsStrategy import ReadResultsStrategy
import numpy as np

class AMLROResultsStrategy(ReadResultsStrategy):
    def analyze_results(self, result_file: str) -> OptimizerResult:
        """Analyzes results from the AMLRO optimizer.

        :param result_file: File to read the results from. This must be
                            formatted as a JSON file.
        :type result_file: str

        :return: Aggregated results from the optimization.
        :rtype: Results
        """

        results = OptimizerResult()
        data = pd.read_csv(result_file)

        max_val = -data["Yield"].max()
        idmax = data["Yield"].idxmax() + 1
        if idmax > 20:
            idmax = idmax - 20
        else:
            idmax = 0

        best_conditions = data.loc[data['Yield'].idxmax()][:-1].values.tolist()
        

        results.raw_results = data
        results.best_coords = best_conditions
        results.best_value = max_val
        results.best_iter = idmax
        results.total_iter = 100

        return results
