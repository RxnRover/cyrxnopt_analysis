from typing import List

from cyrxnopt_analysis.metrics.Metric import Metric
from cyrxnopt_analysis.OptimizerResult import OptimizerResult


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

        # Default the property values
        self._clearance_rate: float = 0
        self._failed_results: List[OptimizerResult] = []
        self._successful_results: List[OptimizerResult] = []

        super(Clearance, self).__init__()

    def calculate(self, results: List[OptimizerResult]):
        """Calculates the clearance rate of the collection of results.

        :param results: Results to use when calculating the metric
        :type results: List[Results]
        """

        # Loop over all results, testing if each one is "successful"
        for result in results:
            # Calculate the error as: (correct - predicted) / correct
            opt_error = self._optimum - result.best_value
            if self._optimum != 0:
                opt_error /= self._optimum

            # If the error is below the threshold, count it
            if abs(opt_error) < self._threshold:
                self._successful_results.append(result)
            else:
                self._failed_results.append(result)

        # Store the success rate
        if self.success_count == 0:
            self._clearance_rate = 0
        else:
            self._clearance_rate = self.success_count / len(results)

        self._result = self._clearance_rate

    @property
    def clearance_rate(self) -> float:
        """Success rate of the optimizer.

        :return: Successful cycle rate out of the number of total cycles.
        :rtype: float
        """

        return self._clearance_rate

    @property
    def fail_count(self) -> int:
        """Number of failed cycles counted.

        :return: Number of failed cycles
        :rtype: int
        """

        return len(self._failed_results)

    @property
    def failed_results(self) -> List[OptimizerResult]:
        """List of only results that failed.

        :return: List of failed result objects.
        :rtype: List[OptimizerResult]
        """

        return self._failed_results

    @property
    def success_count(self) -> int:
        """Number of successful cycles counted.

        :return: Number of successful cycles
        :rtype: int
        """

        return len(self._successful_results)

    @property
    def successful_results(self) -> List[OptimizerResult]:
        """List of only results that were successful.

        :return: List of successful result objects.
        :rtype: List[OptimizerResult]
        """

        return self._successful_results
