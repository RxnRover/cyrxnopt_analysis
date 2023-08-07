import pandas as pd

from pyoptimizer_analysis.OptimizerResult import OptimizerResult
from pyoptimizer_analysis.ReadResultsStrategy import ReadResultsStrategy
from pyoptimizer_analysis.Results import Results
import pandas as pd

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

        #data = df[df['priority'] == -1]
        #data = data.drop('priority', axis=1)
        #data = data.reset_index(drop=True)
        df['yield'] = pd.to_numeric(df[-1])

        max_val = -df['yield'].max()
        idmax = df['yield'].idxmax() + 1

        best_conditions = df.loc[df['yield'].idxmax()][:-2].values.tolist()
        yield_array = df['yield'].values.tolist()

        results.yields = yield_array
        results.best_coords = best_conditions
        results.best_value = max_val
        results.best_iter = idmax
        results.total_iter = 100

        return results
