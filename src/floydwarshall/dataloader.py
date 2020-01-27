import numpy as np

from src.floydwarshall.distance import get_distance
from src.floydwarshall.outlet import Outlet


def generate_outlets():
    outlets = [
        Outlet(0, "Outlet 1", 27.712143, 85.313245),
        Outlet(1, "Outlet 2", 27.712162, 85.312908),
        Outlet(2, "Outlet 3", 27.714843, 85.312044),
        Outlet(3, "Outlet 4", 27.680820, 85.317000),
        Outlet(4, "Outlet 5", 27.686906, 85.317343),
        Outlet(5, "Outlet 6", 27.712020, 85.312950),
    ]
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
