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

    def test_use_budget_property(self):
        budget = 100

        result = OptimizerResult()
        # This will throw with the original budget
        result.total_iter = budget + 1

        alert = OverBudget(budget, throw=True)

        # However, the new budget should allow the previously over-budget
        # iterations
        alert.budget = result.total_iter + 10

        # This shouldn't throw
        alert.process([result])

    def test_set_invalid_budget_property_zero(self):
        alert = OverBudget(100, throw=True)

        # Negative and zero budgets are not allowed
        with self.assertRaises(ValueError):
            alert.budget = 0
        with self.assertRaises(ValueError):
            alert.budget = -1

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

        self.assertTrue(alert.triggered)
        self.assertListEqual(alert.errors, [result2])
