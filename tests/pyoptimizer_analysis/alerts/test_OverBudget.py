import unittest

from pyoptimizer_analysis.alerts.OverBudget import OverBudget
from pyoptimizer_analysis.OptimizerResult import OptimizerResult


class TestOverBudget(unittest.TestCase):
    def test_no_throw_equals_budget_limit(self):
        budget = 100
        result = OptimizerResult()
        result.total_iter = budget

        alert = OverBudget(budget, throw=True)

        # This shouldn't throw
        alert.process([result])

    def test_no_throw_lessthan_budget_limit(self):
        budget = 100

        result = OptimizerResult()
        result.total_iter = budget - 1

        alert = OverBudget(budget, throw=True)

        # This shouldn't throw
        alert.process([result])

    def test_throw_greaterthan_budget_limit(self):
        budget = 100

        result = OptimizerResult()
        result.total_iter = budget + 1

        alert = OverBudget(budget, throw=True)

        self.assertRaises(RuntimeError, alert.process, [result])

    def test_error_list(self):
        budget = 100

        result1 = OptimizerResult()
        result2 = OptimizerResult()
        result3 = OptimizerResult()
        result1.total_iter = budget
        result2.total_iter = budget + 1
        result3.total_iter = budget - 1

        alert = OverBudget(budget, throw=False)

        alert.process([result1, result2, result3])

        self.assertListEqual(alert.errors, [result2])
