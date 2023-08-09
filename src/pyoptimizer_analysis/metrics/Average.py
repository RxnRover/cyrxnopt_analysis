from typing import List

from pyoptimizer_analysis.metrics.Metric import Metric
from pyoptimizer_analysis.OptimizerResult import OptimizerResult


class Average(Metric):
    def __init__(self):
        """Create a Average metric object."""

        self._total_value = 0
        self._total_iterations = 0
        self._average_value = 0

        super(Average, self).__init__()

    def calculate(self, results: List[OptimizerResult]):
        """Calculate the metric.

        :param results: Results to use when calculating the metric
        :type results: List[Results]
        """

        self._total_value = sum([result.best_value for result in results])
        self._total_cycles = len(results)

        # Only update from 0 if there are successful cycles given
        if self._total_cycles != 0:
            self._average_value = self._total_value / self._total_cycles

        self._result = self._average_value

    @property
    def average_value(self) -> float:
        """Averaged optimization iterations needed to reach a successful\
        optimization.

        :return: Average optimization iteration count.
        :rtype: float
        """

        return self._average_value

    @property
    def total_cycles(self) -> int:
        """Number of optimization cycle results used for calculating this
        metric.

        :return: Total cycle count.
        :rtype: int
        """

        return self._total_cycles

    @property
    def total_value(self) -> int:
        """Total summed value of all optimization cycles' best values.

        :return: Sum of best values of cycles.
        :rtype: int
        """

        return self._total_value
