import json

import src.floydwarshall.dataloader as data_loader
from src.core.vrpmanager import Attribute


def create_data_model(outlets):
    data = {}
    parsed_outlet_json = json.loads(outlets)
    outlets = data_loader.generate_outlets(parsed_outlet_json)
    graph = data_loader.get_distance_graph(outlets)

    data[Attribute.OUTLETS] = outlets
    data[Attribute.DISTANCE_MATRIX] = graph
    data[Attribute.DEPOT] = 0
    return data


def distance_callback(distance, from_index, to_index):
    return distance[from_index][to_index]
