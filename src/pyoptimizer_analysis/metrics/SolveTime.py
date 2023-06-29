from typing import List

from pyoptimizer_analysis.metrics.Metric import Metric
from pyoptimizer_analysis.OptimizerResult import OptimizerResult


class SolveTime(Metric):
    def __init__(self):
        """Create a Clearance metric object."""

        self._total_iterations = 0
        self._solve_time = 0

        super(SolveTime, self).__init__()

    def calculate(self, results: List[OptimizerResult]):
        """Calculate the metric.

        :param results: Results to use when calculating the metric
        :type results: List[Results]
        :raises RuntimeError: This function must be overridden by chilren.
        """

        self._total_iterations = sum([result.best_iter for result in results])
        self._total_cycles = len(results)

        self._solve_time = self.total_iterations / self.total_cycles
        self._result = self._solve_time

    @property
    def solve_time(self) -> float:
        """Averaged optimization iterations needed to reach a successful\
        optimization.

        :return: Average optimization iteration count.
        :rtype: float
        """

        return self._solve_time

    @property
    def total_cycles(self) -> int:
        """Number of optimization cycle results used for calculating this
        metric.

        :return: Total cycle count.
        :rtype: int
        """

        return self._total_cycles

    @property
    def total_iterations(self) -> int:
        """Total number of optimization iterations through all of the results
        used to reach the best result.

        :return: Total iteration count.
        :rtype: int
        """

        return self._total_iterations
