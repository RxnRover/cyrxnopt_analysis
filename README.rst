.. image:: https://img.shields.io/badge/Documentation-grey
    :alt: Documentation link
    :target: https://rxnrover.github.io/cyrxnopt_analysis/

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

###################
 cyrxnopt_analysis
###################

    Analysis tools for the example benchmarking for `CyRxnOpt
    <https://github.com/RxnRover/CyRxnOpt>`__.

``cyrxnopt_analysis`` reads the results files from benchmarking `CyRxnOpt
<https://github.com/RxnRover/CyRxnOpt>`__ with `cyrxnopt_server
<https://github.com/RxnRover/cyrxnopt_server>`__, and computes summary metrics
for them, such as clearance rate, solve time, and average error relative to the
known optimum for each benchmark problem. Results are read from a directory of
run output, aggregated per benchmark function, and written out as CSV summaries
for further analysis.

**************
 Installation
**************

Clone the repository and install it with pip:

.. code-block:: bash

    git clone https://github.com/RxnRover/cyrxnopt_analysis.git
    cd cyrxnopt_analysis
    pip install .

**********
 Analysis
**********

A set of results is analyzed with the ``analyze_results`` command-line tool,
installed as part of this package. It takes the optimizer whose results are
being analyzed and the directory containing the results files, and writes CSV
summaries to an output directory (``analysis/{YYYY-MM-DD}_{optimizer}`` by
default).

At minimum, it needs the optimizer that produced the results and the directory
containing the results files to analyze. Run ``analyze_results --help`` for the
full set of options, including the clearance threshold, the file pattern used to
find results files, and where output is written. By default, CSV summaries are
written to ``analysis/{YYYY-MM-DD}_{optimizer}``.

For example, continuing from the ``cyrxnopt_server`` benchmarking example (see
its `README
<https://github.com/RxnRover/cyrxnopt_server/blob/main/README.rst#benchmarking>`__),
which runs the ``random`` optimizer and writes results to
``data/random_optimizer``, the results can be analyzed with:

.. code-block:: bash

    analyze_results random ../cyrxnopt_server/data/random_optimizer/ -fp "results\.csv" -t 0.02

*******************************
 Making Changes & Contributing
*******************************

This project uses pre-commit_, please make sure to install it before making any
changes:

.. code-block:: bash

    # After cloning the repository
    pip install pre-commit
    cd cyrxnopt_analyzer
    pre-commit install

.. _pre-commit: https://pre-commit.com/
