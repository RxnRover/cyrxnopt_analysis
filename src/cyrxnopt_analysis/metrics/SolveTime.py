from typing import List

import numpy as np
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

        solve_times = np.array(
            [result.best_iter for result in results], dtype=float
        )

        self._total_iterations = np.sum(solve_times)
        self._total_cycles = len(results)

        if self._total_cycles > 0:
            self._solve_time_mean = np.mean(solve_times)
            self._solve_time_std = np.std(solve_times, ddof=1)

            # optional
            self._solve_time_sem = self._solve_time_std / np.sqrt(
                self._total_cycles
            )

            self._solve_time_ci95 = 1.96 * self._solve_time_sem

        else:
            self._solve_time_mean = np.nan
            self._solve_time_std = np.nan
            self._solve_time_sem = np.nan
            self._solve_time_ci95 = np.nan

        self._result = self._solve_time_mean

    @property
    def solve_time(self) -> float:
        """Averaged optimization iterations needed to reach a successful\
        optimization.

        :return: Average optimization iteration count.
        :rtype: float
        """

        return self._solve_time_mean

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

    @property
    def solve_time_std(self) -> int:
        """Standard deviation of average optimization iterations needed to
        reach a successful optimization.

        :return: Std.
        :rtype: float
        """

        return self._solve_time_std

    @property
    def solve_time_CI95(self) -> int:
        """CI 95% of average optimization iterations needed to reach a successful\
        optimization.

        :return: CI
        :rtype: float
        """

        return self._solve_time_ci95
