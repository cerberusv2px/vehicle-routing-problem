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


def get_json_outlets():
    data = """{
  "outlets": [
        {
            "id": 2,
            "latitude": 27.699000636894265,
            "longitude": 85.30949768849477,
            "name": "Gurung - Niroula"
        },
        {
            "id": 1,
            "latitude": 27.70502375671876,
            "longitude": 85.32964735689039,
            "name": "Bastola, Sherpa and Lama"
        },
        {
            "id": 3,
            "latitude": 27.70585290494114,
            "longitude": 85.326131396724,
            "name": "Gurung, Lama and Gurung"
        },
        {
            "id": 4,
            "latitude": 27.688060771990116,
            "longitude": 85.34052083017637,
            "name": "Maharjan Ltd"
        },
        {
            "id": 5,
            "latitude": 27.687371818264367,
            "longitude": 85.33464417645206,
            "name": "Pradhan, Dhakal and Ghale"
        },
        {
            "id": 6,
            "latitude": 27.699391850832637,
            "longitude": 85.31947756429923,
            "name": "Rana - Aryal"
        },
        {
            "id": 7,
            "latitude": 27.70112815556888,
            "longitude": 85.30603392195476,
            "name": "Thapa, Aryal and Raut"
        },
        {
            "id": 8,
            "latitude": 27.69104398076337,
            "longitude": 85.32450992923185,
            "name": "Bhattarai, Koirala and Shrestha"
        },
        {
            "id": 9,
            "latitude": 27.69782791962137,
            "longitude": 85.34373969578154,
            "name": "Karki - Raut"
        },
        {
            "id": 10,
            "latitude": 27.682079277113576,
            "longitude": 85.31857901527917,
            "name": "Khadka, Kafle and Adhikari"
        },
        {
            "id": 11,
            "latitude": 27.691036354937673,
            "longitude": 85.33328595288458,
            "name": "Bhandari Limited"
        },
        {
            "id": 12,
            "latitude": 27.69340209170034,
            "longitude": 85.3262768578779,
            "name": "Adhikari - Baral"
        },
        {
            "id": 13,
            "latitude": 27.688199603985318,
            "longitude": 85.32705360452886,
            "name": "Chettri, Shrestha and Ghale"
        },
        {
            "id": 14,
            "latitude": 27.682808490940584,
            "longitude": 85.32453882594136,
            "name": "Dhakal, Tamang and Tamang"
        },
        {
            "id": 15,
            "latitude": 27.68297868819958,
            "longitude": 85.32382136232778,
            "name": "Pandey Pvt Ltd"
        },
        {
            "id": 16,
            "latitude": 27.680753458213292,
            "longitude": 85.33187608482363,
            "name": "Pradhan, Sai and KC"
        },
        {
            "id": 17,
            "latitude": 27.680528680951358,
            "longitude": 85.32368560261718,
            "name": "Basnet - Lama"
        },
        {
            "id": 18,
            "latitude": 27.69170270565424,
            "longitude": 85.3155649454502,
            "name": "Shrestha - Jung"
        },
        {
            "id": 19,
            "latitude": 27.69689460866066,
            "longitude": 85.34219874554468,
            "name": "Maharjan Ltd"
        },
        {
            "id": 20,
            "latitude": 27.69249164163872,
            "longitude": 85.33017395989891,
            "name": "Kafle, Baral and Basynat"
        },
        {
            "id": 21,
            "latitude": 27.706699865937157,
            "longitude": 85.32824803549654,
            "name": "Niroula, Basynat and Thapa"
        },
        {
            "id": 22,
            "latitude": 27.68499640778519,
            "longitude": 85.3311833110298,
            "name": "Magar - Sherpa"
        },
        {
            "id": 23,
            "latitude": 27.691099135275476,
            "longitude": 85.33298043438053,
            "name": "Dongol, Raut and Gurung"
        },
        {
            "id": 24,
            "latitude": 27.681227532511436,
            "longitude": 85.32928212859302,
            "name": "Basynat, Ghale and Adhikari"
        },
        {
            "id": 25,
            "latitude": 27.69915562975916,
            "longitude": 85.32628658406632,
            "name": "Rana Pvt Ltd"
        },
        {
            "id": 26,
            "latitude": 27.697166627848173,
            "longitude": 85.32753136082722,
            "name": "Lama Ltd"
        },
        {
            "id": 27,
            "latitude": 27.69700696813413,
            "longitude": 85.33622642750214,
            "name": "Kafle, Gyawali and Devkota"
        },
        {
            "id": 28,
            "latitude": 27.699532045230654,
            "longitude": 85.32994735326197,
            "name": "Limbu - Pradhan"
        },
        {
            "id": 29,
            "latitude": 27.699796932990058,
            "longitude": 85.32560847371708,
            "name": "Chettri - Subedi"
        },
        {
            "id": 30,
            "latitude": 27.704900231704695,
            "longitude": 85.3236632964715,
            "name": "Khadka Group"
        },
        {
            "id": 31,
            "latitude": 27.684701257312337,
            "longitude": 85.31326804429808,
            "name": "Ghale Group"
        },
        {
            "id": 32,
            "latitude": 27.700972711778338,
            "longitude": 85.31713074506645,
            "name": "Lama Ltd"
        },
        {
            "id": 33,
            "latitude": 27.685836111526505,
            "longitude": 85.31494874590965,
            "name": "Dongol Pvt Ltd"
        },
        {
            "id": 34,
            "latitude": 27.679119636810473,
            "longitude": 85.3203262351637,
            "name": "Raut, Bhattarai and Gurung"
        },
        {
            "id": 35,
            "latitude": 27.700805992050277,
            "longitude": 85.33170122958396,
            "name": "Magar - Maharjan"
        },
        {
            "id": 36,
            "latitude": 27.6867779324489,
            "longitude": 85.30904806899792,
            "name": "Baral - Gyawali"
        },
        {
            "id": 37,
            "latitude": 27.693676322564823,
            "longitude": 85.34147812204269,
            "name": "Kafle - Shrestha"
        },
        {
            "id": 38,
            "latitude": 27.699215556077643,
            "longitude": 85.33503438099599,
            "name": "Bhattarai, Dhakal and Raut"
        },
        {
            "id": 39,
            "latitude": 27.703647056349006,
            "longitude": 85.31700988960587,
            "name": "Karki - Thapa"
        },
        {
            "id": 40,
            "latitude": 27.708011721619705,
            "longitude": 85.3131784715225,
            "name": "Rana, Shrestha and Subedi"
        },
        {
            "id": 41,
            "latitude": 27.702638833883974,
            "longitude": 85.32420566926483,
            "name": "Jung Group"
        },
        {
            "id": 42,
            "latitude": 27.707601924691986,
            "longitude": 85.31201362911375,
            "name": "Jung, Pradhan and Gyawali"
        },
        {
            "id": 43,
            "latitude": 27.681540128469962,
            "longitude": 85.31697333766712,
            "name": "Shakya - Basynat"
        },
        {
            "id": 44,
            "latitude": 27.684471492693394,
            "longitude": 85.32184101394245,
            "name": "Kafle - Thapa"
        },
        {
            "id": 45,
            "latitude": 27.684728992053877,
            "longitude": 85.31828526985738,
            "name": "Basnet Limited"
        },
        {
            "id": 46,
            "latitude": 27.693580651745584,
            "longitude": 85.34182841468112,
            "name": "Jung - Karki"
        },
        {
            "id": 47,
            "latitude": 27.702160700428273,
            "longitude": 85.31655253718223,
            "name": "Lama Limited"
        },
        {
            "id": 48,
            "latitude": 27.71054982427886,
            "longitude": 85.32640255215468,
            "name": "Gyawali - Maharjan"
        },
        {
            "id": 49,
            "latitude": 27.70114962873887,
            "longitude": 85.33771261798655,
            "name": "Hamal - Ghale"
        },
        {
            "id": 50,
            "latitude": 27.701682502482676,
            "longitude": 85.31185390373238,
            "name": "Magar, Hamal and Aryal"
        }
    ]
}"""
    return data
