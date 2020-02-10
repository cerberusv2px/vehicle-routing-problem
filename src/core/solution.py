import json
from src.core.vrpmanager import VRPManager, Strategy, Attribute

DSE = "dse"
OUTLETS = "outlets"


def _handle_cheap_path_strategy(vrp_manager, data):
    results = []
    max_route_distance = 0.0
    for dse in range(vrp_manager.num_dse):
        outcome = {}
        index = 0
        outcome[DSE] = dse
        outcome[OUTLETS] = []
        route_distance = 0.0

        while route_distance < vrp_manager.max_distance or len(outcome[OUTLETS]) < vrp_manager.max_outlets:
            outcome[OUTLETS].append(json.loads(data[Attribute.OUTLETS][index].toJSON()))
            previous_index = index


    return results


def _handle_time_efficient_strategy(vrp_manager, data):
    return []


def get_solution(vrp_manager: VRPManager, data):
    if vrp_manager.strategy == Strategy.SHORTEST_PATH:
        _handle_cheap_path_strategy(vrp_manager, data)
    else:
        _handle_time_efficient_strategy(vrp_manager, data)
    return 0
