import os
import re
from typing import List

from cyrxnopt_analysis.OptimizerResult import OptimizerResult
from cyrxnopt_analysis.transforms.Transform import Transform


class GetFunctionName(Transform):
    @staticmethod
    def map(results: List[OptimizerResult]):
        """Get the function name for each result based on the result file's
        containing directory. The function name will be stored in the
        result object under the "function" key.

        :param results: Result list to transform.
        :type results: List[OptimizerResult]
        """

        results = list(map(GetFunctionName._get_function_name, results))

        return results

    @staticmethod
    def _get_function_name(result):
        """Extracts the function name from the containing directory of
        the results file and stores it in the Result object under the
        "function" key.

        :param result: Result object to get the function name for.
        :type result: OptimizerResult
        :return: Result object with the function name
        :rtype: OptimizerResult
        """

        directory = os.path.basename(os.path.dirname(result.filename))
        match = re.match(r"([a-zA-Z0-9_]+)_[0-9]+", directory)

        if not match:
            raise RuntimeError(
                "No function name found in file path! Path: {}".format(
                    result.filename
                )
            )

        foo_name = match[1]

        result["function"] = foo_name

        return result
