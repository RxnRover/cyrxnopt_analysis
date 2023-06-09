from pyoptimizer_analysis.ReadResultsStrategy import ReadResultsStrategy


class SQSnobFitResultsStrategy(ReadResultsStrategy):
    def analyze_results(self, result_file: str):
        raise RuntimeError("ReadResultsStrategy.analyze_results not overridden!")
