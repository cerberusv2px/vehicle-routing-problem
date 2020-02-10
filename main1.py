import src.core.utils as vrp_utils
import src.floydwarshall.dataloader as data_loader
from src.core.solution import get_solution
from src.core.vrpmanager import VRPManager, Strategy


def main():
    manager = VRPManager(max_distance=5.0, max_outlets=30, num_dse=3, strategy=Strategy.SHORTEST_PATH)
    data = vrp_utils.create_data_model(outlets=data_loader.get_json_outlets())
    get_solution(vrp_manager=manager, data=data)


if __name__ == '__main__':
    main()
