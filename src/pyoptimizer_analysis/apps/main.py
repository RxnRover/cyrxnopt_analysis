import argparse
import json

from pyoptimizer_analysis.AMLROResultsStrategy import AMLROResultsStrategy
from pyoptimizer_analysis.Analyzer import Analyzer
from pyoptimizer_analysis.EDBOpResultsStrategy import EDBOpResultsStrategy
from pyoptimizer_analysis.NMSimplexResultsStrategy import NMSimplexResultsStrategy
from pyoptimizer_analysis.SQSnobFitResultsStrategy import SQSnobFitResultsStrategy


def parse_args() -> argparse.Namespace:
    """Parse command line arguments"""

    parser = argparse.ArgumentParser()

    # parser.add_argument("output_dir", help="Location for output data.")
    parser.add_argument("optimizer", help="Optimizer to use.")
    parser.add_argument("results_file", help="Location for results file to analyze.")
    # parser.add_argument(
    #     "--default-config",
    #     action="store_true",
    #     help=(
    #         "Generate config file with default values at the location given by"
    #         " output_dir."
    #     ),
    # )

    args = parser.parse_args()

    return args


def main():
    """Starting point for using an optimizer with zmq"""

    args = parse_args()

    optimizer_lower = args.optimizer.lower()

    if optimizer_lower == "amlro":
        results_strategy = AMLROResultsStrategy()
    elif optimizer_lower == "edbop":
        results_strategy = EDBOpResultsStrategy()
    elif optimizer_lower == "nmsimplex":
        results_strategy = NMSimplexResultsStrategy()
    elif optimizer_lower == "sqsnobfit":
        results_strategy = SQSnobFitResultsStrategy()
    else:
        raise RuntimeError("Invalid optimizer provided: {}".format(args.optimizer))

    analyzer = Analyzer(results_strategy)

    results = analyzer.analyze_results(args.results_file)

    print(results)
    print(json.dumps(results))


if __name__ == "__main__":
    main()
