import statistics
from typing import List

from pyoptimizer_analysis.metrics.Metric import Metric
from pyoptimizer_analysis.OptimizerResult import OptimizerResult


class StdDev(Metric):
    def __init__(self):
        """Create a Average metric object."""

        self._sample_set = []
        self._total_cycles = 0
        self._stddev = 0

        super(StdDev, self).__init__()

    def calculate(self, results: List[OptimizerResult]):
        """Calculate the metric.

        :param results: Results to use when calculating the metric
        :type results: List[Results]
        """

        self._sample_set = [result.best_value for result in results]
        self._total_cycles = len(results)

        # At least two data points are needed to calculate std dev
        if len(results) >= 2:
            self._stddev = statistics.stdev(self._sample_set)

        self._result = self._stddev

    @property
    def sample_set(self) -> int:
        """Sample set of best values to calculate Std. Dev. on.

        :return: Sample set of best values.
        :rtype: int
        """

        return self._sample_set

    @property
    def stddev(self) -> float:
        """Standard deviation of optimization iterations' best values.

        :return: Standard deviation of best values.
        :rtype: float
        """

        return self._stddev

    @property
    def total_cycles(self) -> int:
        """Number of optimization cycle results used for calculating this
        metric.

        :return: Total cycle count.
        :rtype: int
        """

        return self._total_cycles
