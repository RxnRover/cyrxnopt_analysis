from pyoptimizer_analysis.ReadResultsStrategy import ReadResultsStrategy


class Analyzer:
    def __init__(self, read_strategy: ReadResultsStrategy):
        self._read_strategy = read_strategy

    def analyze_results(self, results_file: str):
        return self._read_strategy.analyze_results(results_file)

    # def analyze_directory(self, results_directory: str):

    #     # Read all the files os.walk

    #     for result_file in files:

    #         result = self.analyze_results(result_file)
