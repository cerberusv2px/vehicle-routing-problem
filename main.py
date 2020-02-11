import json
import sys

from ortools.constraint_solver import routing_enums_pb2, pywrapcp

import src.floydwarshall.dataloader as dataloader

DISTANCE_MATRIX = "distance_matrix"
NUM_VEHICLE = "num_vehicles"
DEPOT = "depot"
OUTLETS = "outlets"
DSE = "dse"
TRAVEL = "travel"
DISTANCE = "distance"


def create_data_model(outlet_inputs, num_vehicle):
    parsed_json = json.loads(dataloader.get_json_outlets())
    data = {}
    outlets = dataloader.generate_outlets(parsed_json)
    graph = dataloader.get_distance_graph(outlets)
    data[OUTLETS] = outlets
    data[DISTANCE_MATRIX] = graph
    data[NUM_VEHICLE] = int(num_vehicle)
    data[DEPOT] = 0
    # data = {DISTANCE_MATRIX: dataloader.get_random_data(50), NUM_VEHICLE: 3, DEPOT: 0}
    return data


def print_solution(data, manager, routing, solution):
    print(data[DISTANCE_MATRIX])
    results = []
    total_distance = 0.0
    max_route_distance = 0.0
    for vehicle_id in range(data[NUM_VEHICLE]):
        outcome = {}
        index = routing.Start(vehicle_id)
        outcome[DSE] = vehicle_id
        outcome[TRAVEL] = []
        plan_output = 'Route for DSE {}:\n'.format(vehicle_id)
        route_distance = 0.0

        while not routing.IsEnd(index):
            outcome[TRAVEL].append(json.loads(data[OUTLETS][manager.IndexToNode(index)].toJSON()))
            plan_output += '{} -> '.format(data[OUTLETS][manager.IndexToNode(index)].name)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            arc_cost = routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            route_distance += arc_cost
            # if index < len(DISTANCE_MATRIX):
            # route_distance += data[DISTANCE_MATRIX][previous_index][index]
            # print(arc_cost)

        outcome[TRAVEL].append(json.loads(data[OUTLETS][manager.IndexToNode(index)].toJSON()))
        outcome[DISTANCE] = route_distance
        plan_output += '{}\n'.format(data[OUTLETS][manager.IndexToNode(index)].name)
        plan_output += 'Distance route: {}km\n'.format(route_distance)
        print(plan_output)
        max_route_distance = max(route_distance, max_route_distance)
        total_distance += route_distance
        results.append(outcome)
    print('Max of route distances: {}km'.format(max_route_distance))
    print('total distance: {}km'.format(total_distance))
    return results


def get_routes(manager, routing, solution, num_routes):
    """Get vehicle routes from a solution and store them in an array."""
    # Get vehicle routes and store them in a two dimensional array whose
    # i,j entry is the jth location visited by vehicle i along its route.
    routes = []
    for route_nbr in range(num_routes):
        index = routing.Start(route_nbr)
        route = [manager.IndexToNode(index)]
        while not routing.IsEnd(index):
            index = solution.Value(routing.NextVar(index))
            route.append(manager.IndexToNode(index))
        routes.append(route)
    return routes


def main():
    # Instantiate the data problem
    """
    args[1] = data input
    args[2] = number of vehicles
    """
    data = create_data_model([], 3)

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
        0,  # no slack 5
        5,  # vehicle max travel distance 3
        True,
        dimension_name
    )

    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(10)

    # Setting first solution heuristic
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )

    # Solve problem
    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        routes = get_routes(manager, routing, solution, data[NUM_VEHICLE])
        for i, route in enumerate(routes):
            print('Route', i, route)

        result = print_solution(data, manager, routing, solution)
        # print(result)
        sys.stdout.flush()
    else:
        print("""
        {
            "message": "Solution not found. Might be due to dse counts or max distance travelled parameter"
        }
        """)
        sys.stdout.flush()


if __name__ == '__main__':
    main()
