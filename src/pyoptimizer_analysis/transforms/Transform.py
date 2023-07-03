from abc import ABC
from typing import List

from pyoptimizer_analysis.OptimizerResult import OptimizerResult


class Transform(ABC):
    def map(self, results: List[OptimizerResult]):
        """Apply the transform to the list of results.

        :param results: Results to transform
        :type results: List[OptimizerResult]
        :raises RuntimeError: This function must be overridden by chilren.
        """

        raise RuntimeError("Transform.map not overridden!")  # pragma: no cover
