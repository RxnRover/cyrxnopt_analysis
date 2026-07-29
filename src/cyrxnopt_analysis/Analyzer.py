from typing import List

from cyrxnopt_analysis.OptimizerResult import OptimizerResult
from cyrxnopt_analysis.ReadResultsStrategy import ReadResultsStrategy
from cyrxnopt_analysis.utilities.get_files import get_files


class Analyzer:
    def __init__(self, read_strategy: ReadResultsStrategy):
        self._read_strategy = read_strategy

    def analyze_results(self, results_file: str) -> OptimizerResult:
        """Analyzes the given file, accumulating the results for an
        optimization algorithm.

        The algorithm used to analyze the file is determined by the value
        of read_strategy provided when the Analyzer was created.

        :param results_file: Full path to the results file to analyze.
        :type results_file: str
        :return: Results object containing the results of the optimization.
        :rtype: Results
        """

        results = self._read_strategy.analyze_results(results_file)
        if results is not None:
            results.filename = results_file

        return results

    def analyze_directory(
        self,
        results_directory: str,
        file_pattern: str = r"*",
        recursive: bool = False,
    ) -> List[OptimizerResult]:
        """Analyzes all files in the given directory that match the provided
        regex pattern.

        The results files must all be in the same format to be read correctly.
        If results files are in a different format, incorrect results may be
        collected or the program may crash.
        The algorithm used to analyze the file is determined by the value
        of read_strategy provided when the Analyzer was created.

        :param results_directory: Full path to the results directory with
                                  results files to analyze.
        :type results_directory: str
        :param file_pattern: Regex pattern that result files must match,
                             defaults to r"*" for all files.
        :type file_pattern: str
        :param recursive: Whether to find files recursively in subdirectories
                      (True) or not (False). Defaults to "False".
        :type recursive: bool, optional
        :return: Results object containing the results of the optimization.
        :rtype: Results
        """

        files = get_files(results_directory, file_pattern, recursive=recursive)

        results = []
        for result_file in files:
            result = self.analyze_results(result_file)

            if result is not None:
                results.append(result)

        return results
