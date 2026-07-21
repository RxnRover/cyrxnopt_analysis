import argparse
from datetime import datetime
from pathlib import Path

import pandas as pd

# from cyrxnopt_analysis.alerts.OverBudget import OverBudget
from cyrxnopt_analysis.AMLROResultsStrategy import AMLROResultsStrategy
from cyrxnopt_analysis.Analyzer import Analyzer
from cyrxnopt_analysis.EDBOpResultsStrategy import EDBOpResultsStrategy
from cyrxnopt_analysis.metrics.Average import Average
from cyrxnopt_analysis.metrics.Clearance import Clearance
from cyrxnopt_analysis.metrics.SolveTime import SolveTime
from cyrxnopt_analysis.metrics.StdDev import StdDev
from cyrxnopt_analysis.NMSimplexResultsStrategy import NMSimplexResultsStrategy
from cyrxnopt_analysis.SQSnobFitResultsStrategy import SQSnobFitResultsStrategy
from cyrxnopt_analysis.transforms.GetFunctionName import GetFunctionName
from cyrxnopt_analysis.utilities.optima_table import optima


def parse_args() -> argparse.Namespace:
    """Parse command line arguments"""

    parser = argparse.ArgumentParser()

    # parser.add_argument("output_dir", help="Location for output data.")
    parser.add_argument("optimizer", help="Optimizer to use.")
    parser.add_argument(
        "results_dir", help="Location for results file to analyze."
    )
    parser.add_argument(
        "-t",
        "--threshold",
        default=0.02,
        type=float,
        help=("Clearance rate error threshold. Defaults to 0.02."),
    )
    parser.add_argument(
        "-fp",
        "--filepattern",
        default="results.json",
        type=str,
        help=(
            "File regex pattern to search for results files. Defaults to "
            '"results.json"'
        ),
    )
    parser.add_argument(
        "-o",
        "--outdir",
        default=None,
        type=str,
        help=(
            "Output directory for all analysis results."
            'Defaults to "analysis/{YYYY-MM-DD}_{optimizer}"'
        ),
    )
    parser.add_argument(
        "--results-filename",
        default=None,
        type=str,
        help=(
            "Filename to save the per-function analysis summary CSV to "
            "(clearance rate, average successful value, solve time, "
            "solve time std, and solve time CI95). Defaults to "
            '"{outdir}/{optimizer}_summary.csv".'
        ),
    )

    args = parser.parse_args()

    return args


def main():
    """Entry point to an analysis script."""

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
        raise RuntimeError(
            "Invalid optimizer provided: {}".format(args.optimizer)
        )

    # Default to an output directory if none given
    if args.outdir is None:
        outdir = Path("analysis")
        outdir /= f"{datetime.today().strftime("%Y-%m-%d")}_{optimizer_lower}"

    # Ensure that outdir is a path
    outdir = Path(outdir)

    # Create the output directory if it doesn't exist
    if not outdir.exists():
        outdir.mkdir(exist_ok=True, parents=True)

    analyzer = Analyzer(results_strategy)

    results = analyzer.analyze_directory(
        args.results_dir, file_pattern=args.filepattern, recursive=True
    )
    # if optimizer_lower == "amlro":
    #     results = analyzer.analyze_directory(
    #         args.results_dir, file_pattern=r"training_set_file.txt", recursive=True
    #     )
    # elif optimizer_lower == "edbop":
    #     results = analyzer.analyze_directory(
    #     args.results_dir, file_pattern=r"my_optimization.csv", recursive=True
    # )

    # results = analyzer.analyze_directory(
    #    args.results_dir, file_pattern=r"results.json", recursive=True
    # )

    # Data validation

    # # Check if any of the results went over the budget
    # over_budget = OverBudget(100, throw=False)
    # over_budget.process(results)
    # print("Number of errors: ", len(over_budget.errors))

    # for error in over_budget.errors:
    #     print(error.filename)
    #     print(error.total_iter)

    # if len(over_budget.errors):
    #     raise RuntimeError("Over budget!")

    # Data transforms

    # Get the function used for each result
    results = GetFunctionName.map(results)

    # Metric calculations

    cleared_runs_tbl = pd.DataFrame(columns=["Cleared runs"])
    iterations_tbl = pd.DataFrame(columns=["Iterations needed"])

    cleared_runs_tbl["Cleared runs"] = [optimizer_lower]
    iterations_tbl["Iterations needed"] = [optimizer_lower]

    summary_rows = []

    for foo in optima.keys():
        filtered_results = [x for x in results if x["function"] == foo]
        print("# of results for {}: {}".format(foo, len(filtered_results)))

        if len(filtered_results) == 0:
            print("=" * 40)
            continue

        clearance = Clearance(optima[foo], threshold=args.threshold)
        clearance.calculate(filtered_results)
        print("Clearance rate: ", clearance.clearance_rate)

        solve_time = SolveTime()
        solve_time.calculate(clearance.successful_results)
        print("Solve time: ", solve_time.solve_time)
        print("Solve time Std: ", solve_time.solve_time_std)
        print("Solve time CI95: ", solve_time.solve_time_CI95)

        average_value_successful = Average()
        average_value_successful.calculate(clearance.successful_results)
        if optima[foo] != 0:
            average_value_successful_error = (
                optima[foo] - average_value_successful.result
            ) / optima[foo]
        else:
            average_value_successful_error = (
                optima[foo] - average_value_successful.result
            )
        print(
            "Average successful value: {:.3f}, {:.3f} error".format(
                average_value_successful.result, average_value_successful_error
            )
        )

        std_dev_value_successful = StdDev()
        std_dev_value_successful.calculate(clearance.successful_results)
        print(
            "std_dev successful value: {:.3f}".format(
                std_dev_value_successful.result
            )
        )

        average_value_total = Average()
        average_value_total.calculate(filtered_results)
        if optima[foo] != 0:
            average_value_total_error = (
                optima[foo] - average_value_total.result
            ) / optima[foo]
        else:
            average_value_total_error = optima[foo] - average_value_total.result
        print(
            "Average total value: {:.3f}, {:.3f} error".format(
                average_value_total.result, average_value_total_error
            )
        )

        std_dev_value_total = StdDev()
        std_dev_value_total.calculate(filtered_results)
        print("std_dev total value: {:.3f}".format(std_dev_value_total.result))

        print("Real optimum:", optima[foo])

        # Add data to the dataframes
        cleared_runs_tbl[foo] = [clearance.success_count]
        iterations_tbl[foo] = [solve_time.total_iterations]

        summary_rows.append(
            {
                "function": foo,
                "clearance_rate": clearance.clearance_rate,
                "average_successful_value": average_value_successful.result,
                "solve_time": solve_time.solve_time,
                "solve_time_std": solve_time.solve_time_std,
                "solve_time_ci95": solve_time.solve_time_CI95,
            }
        )

        print("=" * 40)

    cleared_runs_tbl.to_csv(
        outdir / f"{optimizer_lower}_no_noise_clearance.csv", index=False
    )
    iterations_tbl.to_csv(
        outdir / f"{optimizer_lower}_no_noise_iterations.csv", index=False
    )

    results_filename = outdir / (
        args.results_filename or f"{optimizer_lower}_summary.csv"
    )
    pd.DataFrame(summary_rows).to_csv(results_filename, index=False)

    print(cleared_runs_tbl)
    print(iterations_tbl)


if __name__ == "__main__":
    main()
