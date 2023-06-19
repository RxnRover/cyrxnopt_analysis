from typing import List

from pyoptimizer_analysis.metrics.Metric import Metric
from pyoptimizer_analysis.OptimizerResult import OptimizerResult


class Clearance(Metric):
    def __init__(self, optimum: float, threshold: float = 0.01):
        """Create a Clearance metric object.

        :param optimum: Optimum to check against results.
        :type optimum: float
        :param threshold: Optimization error that an optimizer must achieve
                          to be considered a "success". Defaults to 0.01.
        :type threshold: float, optional
        """

        self._optimum = optimum
        self._threshold = threshold

        super(Clearance, self).__init__()

    def calculate(self, results: List[OptimizerResult]):
        """Calculates the clearance rate of the collection of results.

        :param results: Results to use when calculating the metric
        :type results: List[Results]
        """

        success_count = 0

        # Loop over all results, testing if each one is "successful"
        for result in results:
            # Calculate the error as: (correct - predicted) / correct
            opt_error = self._optimum - result.best_value
            if self._optimum != 0:
                opt_error /= self._optimum

            # If the error is below the threshold, count it
            if opt_error < self._threshold:
                success_count += 1

        # Store the success rate
        if success_count == 0:
            self._result = 0
        else:
            self._result = success_count / len(results)
