import json

import src.core.utils as utils
from src.core.vrpmanager import VRPManager, Strategy, Attribute

DSE = "dse"
OUTLETS = "outlets"

route_index = [0]


def _find_next_outlet(distance_graph, previous_index):
    min_distance = 9999.9
    next_index = -1
    for index, distance in enumerate(distance_graph[previous_index]):
        if min_distance > distance:
            next_index = index
    route_index.append(next_index)
    return next_index


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
            next_index = _find_next_outlet(data[Attribute.DISTANCE_MATRIX], previous_index)
            outcome[OUTLETS].append(json.loads(data[Attribute.OUTLETS][next_index].toJSON()))
            route_distance += utils.distance_callback(data[Attribute.DISTANCE_MATRIX], previous_index, next_index)

    return results


def _handle_time_efficient_strategy(vrp_manager, data):
    return []


def get_solution(vrp_manager: VRPManager, data):
    if vrp_manager.strategy == Strategy.SHORTEST_PATH:
        _handle_cheap_path_strategy(vrp_manager, data)
    else:
        _handle_time_efficient_strategy(vrp_manager, data)
    return 0
