from typing import List

from pyoptimizer_analysis.metrics.Metric import Metric
from pyoptimizer_analysis.OptimizerResult import OptimizerResult


class SolveTime(Metric):
    def __init__(self, budget: int = 100):
        """Create a SolveTime metric object.

        :param optimum: Optimum to check against results.
        :type optimum: float
        """

        self._budget = 100

        super(SolveTime, self).__init__()

    def calculate(self, results: List[OptimizerResult]):
        """Calculate the metric.

        :param results: Results to use when calculating the metric
        :type results: List[Results]
        :raises RuntimeError: This function must be overridden by chilren.
        """

        solve_time = 0
        count = 0

        for result in results:
            # if result.best_iter != self._budget:
            solve_time += result.best_iter
            count += 1

        # Exit early if no results found a satisfactory solution
        if count == 0:
            solve_time = 0
        else:
            solve_time /= count

        self._result = solve_time
