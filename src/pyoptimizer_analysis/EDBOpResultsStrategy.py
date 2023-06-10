from pyoptimizer_analysis.ReadResultsStrategy import ReadResultsStrategy
from pyoptimizer_analysis.Results import Results
import pandas as pd

class EDBOpResultsStrategy(ReadResultsStrategy):
    def analyze_results(self, result_file: str)-> Results:
        """Analyzes results from the EDBOP optimizer.

        :param result_file: File to read the results from. This must be
                            formatted as a JSON file.
        :type result_file: str

        :return: Aggregated results from the optimization.
        :rtype: Results
        """
        
        results = Results()
        df = pd.read_csv(result_file)
        data = df[df['priority']==-1]
        data = data.drop('priority', axis=1)
        data = data.reset_index(drop=True)
        data['yield'] = pd.to_numeric(data['yield'])
        print(data)

        max_val = -data['yield'].max()
        idmax = data['yield'].idxmax()+1

        best_conditions = data.loc[data['yield'].idxmax()][:-1].values.tolist()

        results.best_coords = best_conditions
        results.best_value = max_val
        results.best_iter = idmax
        results.total_iter = 100
        return results
