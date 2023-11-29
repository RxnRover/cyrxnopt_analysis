from abc import ABC
from typing import Any, List

from cyrxnopt_analysis.OptimizerResult import OptimizerResult


class Metric(ABC):
    def __init__(self):
        self._result = None

    def calculate(self, results: List[OptimizerResult]):
        """Calculate the metric.

        :param results: Results to use when calculating the metric
        :type results: List[Results]
        :raises RuntimeError: This function must be overridden by chilren.
        """

        raise RuntimeError(
            "Metric.calculate not overridden!"
        )  # pragma: no cover

    @property
    def result(self) -> Any:
        return self._result
