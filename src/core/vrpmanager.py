from enum import Enum

"""
VRP Manager for mostly handling the configuration.
"""


class Strategy(Enum):
    SHORTEST_PATH = "shortest_path"
    TIME_EFFICIENT = "time_efficient"


class Attribute(Enum):
    OUTLETS = "outlets"
    DISTANCE_MATRIX = "distance_matrix"
    DEPOT = "depot"


class VRPManager:

    def __init__(self, num_dse: int, max_distance: float, max_outlets: int, strategy):
        self.num_dse = num_dse
        self.max_distance = max_distance
        self.max_outlets = max_outlets
        self.strategy = strategy

