from typing import List

from pyoptimizer_analysis.metrics.Metric import Metric
from pyoptimizer_analysis.OptimizerResult import OptimizerResult


class SolveTime(Metric):
    def __init__(self):
        """Create a SolveTime metric object.

        :param optimum: Optimum to check against results.
        :type optimum: float
        """

        super(SolveTime, self).__init__()

    def calculate(self, results: List[OptimizerResult]):
        """Calculate the metric.

        :param results: Results to use when calculating the metric
        :type results: List[Results]
        :raises RuntimeError: This function must be overridden by chilren.
        """

        raise RuntimeError("Metric.calculate not overridden!")
