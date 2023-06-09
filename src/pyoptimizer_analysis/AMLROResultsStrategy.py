from pyoptimizer_analysis.ReadResultsStrategy import ReadResultsStrategy


class AMLROResultsStrategy(ReadResultsStrategy):
    def analyze_results(self, result_file: str):
        raise RuntimeError("ReadResultsStrategy.analyze_results not overridden!")

        # results = Results()

        # results.best_coords = [0, 1]
        # results["approx_min"] =
        # results["approx_best_value"] =
        # results["approx_best_iter"] =

        # return results
