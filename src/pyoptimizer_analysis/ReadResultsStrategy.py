from abc import ABC


class ReadResultsStrategy(ABC):
    def analyze_results(self, result_file: str):
        raise RuntimeError("ReadResultsStrategy.analyze_results not overridden!")
