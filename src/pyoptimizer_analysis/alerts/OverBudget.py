from typing import List

from pyoptimizer_analysis.alerts.Alert import Alert
from pyoptimizer_analysis.Results import Results


class OverBudget(Alert):
    def __init__(self, budget: int, throw: bool = False):
        super(OverBudget, self).__init__(throw)

        self._budget = budget
        self._errors = []

    def process(self, results: List[Results]):
        for result in results:
            # Skip the result if it is not tripping the alarm
            if result.total_iter <= self.budget:
                continue

            # Store the result that is tripping the alarm
            self._errors.append(result)

            # Throw an error
            if self.throw:
                raise RuntimeError("Over budget!")

    @property
    def budget(self) -> int:
        return self._budget

    @budget.setter
    def budget(self, value: int):
        if value < 1:
            raise ValueError("Cannot have a budget of <= 0.")

        self._budget = value

    @property
    def errors(self) -> List[Results]:
        return self._errors
