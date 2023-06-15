from abc import ABC
from typing import List

from pyoptimizer_analysis.Results import Results


class Alert(ABC):
    def __init__(self, throw: bool = False):
        """Create an Alert instance.

        :param throw: Toggle whether the alert should throw an exception when
                      it triggers or not, defaults to False
        :type throw: bool, optional
        """

        self._throw = throw
        self._triggered = False

    def process(self, results: List[Results]):
        """Process the results, triggering the alarm if certain conditions
        are met.

        :param results: Result list to process
        :type results: List[Results]
        :raises RuntimeError: This function must be overridden in children.
        """

        raise RuntimeError("Alert.process is not overridden!")

    @property
    def throw(self) -> bool:
        return self._throw

    @property
    def triggered(self) -> bool:
        return self._triggered
