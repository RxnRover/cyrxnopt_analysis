import pandas as pd

from cyrxnopt_analysis.OptimizerResult import OptimizerResult
from cyrxnopt_analysis.ReadResultsStrategy import ReadResultsStrategy


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

        max_val = -data[data.columns[-1]].max()
        idmax = data[data.columns[-1]].idxmax() + 1
        if idmax > 20:
            idmax = idmax - 20
        else:
            idmax = 0

        best_conditions = data.loc[data[data.columns[-1]].idxmax()][
            :-1
        ].values.tolist()

        results.best_coords = best_conditions
        results.best_value = max_val
        results.best_iter = idmax
        results.total_iter = 100

        return results
