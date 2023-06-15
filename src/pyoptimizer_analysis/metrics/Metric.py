from abc import ABC
from typing import Any, List

from pyoptimizer_analysis.Results import Results


class Metric(ABC):
    def __init__(self):
        self._result = None

    def calculate(self, results: List[Results]):
        """Calculate the metric.

        :param results: Results to use when calculating the metric
        :type results: List[Results]
        :raises RuntimeError: This function must be overridden by chilren.
        """

        raise RuntimeError("Metric.calculate not overridden!")

    @property
    def result(self) -> Any:
        return self._result
