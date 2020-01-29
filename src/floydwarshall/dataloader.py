import numpy as np

from src.floydwarshall.distance import get_distance
from src.floydwarshall.outlet import Outlet


def generate_outlets(data):
    outlets = []
    for outlet in data['outlets']:
        outlets.append(Outlet(outlet['id'], outlet['name'], outlet['latitude'], outlet['longitude']))
    return outlets


def get_random_data(size):
    random_data = np.random.uniform(0, 10, [size, size])
    np.fill_diagonal(random_data, 0)
    return random_data


def get_distance_graph(outlets):
    size = len(outlets)
    distance_graph = np.zeros(shape=(size, size))
    for i in range(len(outlets)):
        outlet = outlets[i]
        for j in range(len(outlets)):
            reference_outlet = outlets[j]
            if i == j:
                distance_graph[i][j] = 0.0
            else:
                distance_graph[i][j] = get_distance(outlet.latitude, outlet.longitude, reference_outlet.latitude,
                                                    reference_outlet.longitude)
    # print(distance_graph)
    return distance_graph
