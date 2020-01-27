from ortools.constraint_solver import routing_enums_pb2, pywrapcp

import src.floydwarshall.dataloader as dataloader

DISTANCE_MATRIX = "distance_matrix"
NUM_VEHICLE = "num_vehicles"
DEPOT = "depot"


def create_data_model():
    data = {DISTANCE_MATRIX: dataloader.get_random_data(50), NUM_VEHICLE: 3, DEPOT: 0}
    # outlets = dataloader.generate_outlets()
    # graph = dataloader.get_distance_graph(outlets)
    # data[DISTANCE_MATRIX] = graph
    return data


def print_solution(data, manager, routing, solution):
    max_route_distance = 0
    for vehicle_id in range(data[NUM_VEHICLE]):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicles {}:\n'.format(vehicle_id)
        route_distance = 0

        while not routing.IsEnd(index):
            plan_output += '{} -> '.format(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)

        plan_output += '{}\n'.format(manager.IndexToNode(index))
        plan_output += 'Distance route: {}km\n'.format(route_distance)
        print(plan_output)
        max_route_distance = max(route_distance, max_route_distance)
    print('Max of route distances: {}km'.format(max_route_distance))


def main():
    # Instantiate the data problem
    data = create_data_model()

    # Create routing index manager
    manager = pywrapcp.RoutingIndexManager(len(data[DISTANCE_MATRIX]), data[NUM_VEHICLE], data[DEPOT])

    # Create routing model
    routing = pywrapcp.RoutingModel(manager)

    # Create and register transit callback
    def distance_callback(from_index, to_index):
        # Returns distance between the two nodes
        # Convert from routing variable Index to distance matrix NodeIndex
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data[DISTANCE_MATRIX][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # define cost of each arc
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # add distance constraint
    dimension_name = "Distance"
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        8,  # vehicle max travel distance
        True,
        dimension_name
    )

    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(5)

    # Setting first solution heuristic
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )

    # Solve problem
    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        print_solution(data, manager, routing, solution)


if __name__ == '__main__':
    main()
