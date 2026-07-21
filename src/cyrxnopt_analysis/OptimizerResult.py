from math import nan


# TODO: I think a dataclass would be better for this
class OptimizerResult(dict):
    def __init__(self):
        self["best_coords"] = []
        self["best_value"] = nan
        self["best_iter"] = -1
        self["filename"] = ""
        self["total_iter"] = -1
        self["message"] = ""
        self["raw_results"] = None

    @property
    def best_coords(self):
        return self["best_coords"]

    @best_coords.setter
    def best_coords(self, value):
        self["best_coords"] = value

    @property
    def best_value(self):
        return self["best_value"]

    @best_value.setter
    def best_value(self, value):
        self["best_value"] = value

    @property
    def best_iter(self):
        return self["best_iter"]

    @best_iter.setter
    def best_iter(self, value):
        self["best_iter"] = value

    @property
    def filename(self) -> str:
        return self["filename"]

    @filename.setter
    def filename(self, value: str):
        self["filename"] = value

    @property
    def total_iter(self):
        return self["total_iter"]

    @total_iter.setter
    def total_iter(self, value):
        self["total_iter"] = value

    @property
    def message(self):
        return self["message"]

    @message.setter
    def message(self, value):
        self["message"] = value

    @property
    def raw_results(self):
        return self["raw_results"]

    @raw_results.setter
    def raw_results(self, value):
        self["raw_results"] = value
