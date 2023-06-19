from benchmarking.functions import (
    branin,
    goldstein_price,
    hartmann,
    rosenbrock,
    shekel,
    shubert,
    six_hump_camel,
)

optima = {
    "branin": branin.branin_min(),
    "goldstein_price": goldstein_price.goldstein_price_min(),
    "hartmann3d": hartmann.hartmann_min(dimensions=3),
    "hartmann6d": hartmann.hartmann_min(dimensions=6),
    "rosenbrock": rosenbrock.rosenbrock_min(),
    "shekel5": shekel.shekel_min(5),
    "shekel7": shekel.shekel_min(7),
    "shekel10": shekel.shekel_min(10),
    "shubert": shubert.shubert_min(),
    "six_hump_camel": six_hump_camel.six_hump_camel_min(),
}
