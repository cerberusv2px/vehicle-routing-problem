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
      "id": 1,
      "name": "Bastola, Sherpa and Lama",
      "latitude": 27.70502375671876,
      "longitude": 85.32964735689039,
      "sequence": 0,
      "lat": 27.70502375671876,
      "lng": 85.32964735689039
    },
    {
      "id": 2,
      "name": "Gurung - Niroula",
      "latitude": 27.699000636894265,
      "longitude": 85.30949768849477,
      "sequence": 0,
      "lat": 27.699000636894265,
      "lng": 85.30949768849477
    },
    {
      "id": 3,
      "name": "Gurung, Lama and Gurung",
      "latitude": 27.70585290494114,
      "longitude": 85.326131396724,
      "sequence": 0,
      "lat": 27.70585290494114,
      "lng": 85.326131396724
    },
    {
      "id": 4,
      "name": "Maharjan Ltd",
      "latitude": 27.688060771990116,
      "longitude": 85.34052083017637,
      "sequence": 0,
      "lat": 27.688060771990116,
      "lng": 85.34052083017637
    },
    {
      "id": 5,
      "name": "Pradhan, Dhakal and Ghale",
      "latitude": 27.687371818264367,
      "longitude": 85.33464417645206,
      "sequence": 0,
      "lat": 27.687371818264367,
      "lng": 85.33464417645206
    },
    {
      "id": 6,
      "name": "Rana - Aryal",
      "latitude": 27.699391850832637,
      "longitude": 85.31947756429923,
      "sequence": 0,
      "lat": 27.699391850832637,
      "lng": 85.31947756429923
    },
    {
      "id": 7,
      "name": "Thapa - Sherpa",
      "latitude": 27.68939185083264,
      "longitude": 85.32947756429922,
      "sequence": 0,
      "lat": 27.68939185083264,
      "lng": 85.3947756429923
    },
    {
      "id": 8,
      "name": "Bhattarai, Koirala and Shrestha",
      "latitude": 27.69104398076337,
      "longitude": 85.32450992923185,
      "sequence": 0,
      "lat": 27.69104398076337,
      "lng": 85.32450992923185
    },
    {
      "id": 9,
      "name": "Karki - Raut",
      "latitude": 27.69782791962137,
      "longitude": 85.34373969578154,
      "sequence": 0,
      "lat": 27.69782791962137,
      "lng": 85.34373969578154
    },
    {
      "id": 10,
      "name": "Khadka, Kafle and Adhikari",
      "latitude": 27.682079277113576,
      "longitude": 85.31857901527917,
      "sequence": 0,
      "lat": 27.682079277113576,
      "lng": 85.31857901527917
    },
    {
      "id": 11,
      "name": "Bhandari Limited",
      "latitude": 27.691036354937673,
      "longitude": 85.33328595288458,
      "sequence": 0,
      "lat": 27.691036354937673,
      "lng": 85.33328595288458
    },
    {
      "id": 12,
      "name": "Adhikari - Baral",
      "latitude": 27.69340209170034,
      "longitude": 85.3262768578779,
      "sequence": 0,
      "lat": 27.69340209170034,
      "lng": 85.3262768578779
    },
    {
      "id": 13,
      "name": "Chettri, Shrestha and Ghale",
      "latitude": 27.688199603985318,
      "longitude": 85.32705360452886,
      "sequence": 0,
      "lat": 27.688199603985318,
      "lng": 85.32705360452886
    },
    {
      "id": 14,
      "name": "Dhakal, Tamang and Tamang",
      "latitude": 27.682808490940584,
      "longitude": 85.32453882594136,
      "sequence": 0,
      "lat": 27.682808490940584,
      "lng": 85.32453882594136
    },
    {
      "id": 15,
      "name": "Pandey Pvt Ltd",
      "latitude": 27.68297868819958,
      "longitude": 85.32382136232778,
      "sequence": 0,
      "lat": 27.68297868819958,
      "lng": 85.32382136232778
    },
    {
      "id": 16,
      "name": "Pradhan, Sai and KC",
      "latitude": 27.680753458213292,
      "longitude": 85.33187608482363,
      "sequence": 0,
      "lat": 27.680753458213292,
      "lng": 85.33187608482363
    },
    {
      "id": 17,
      "name": "Basnet - Lama",
      "latitude": 27.680528680951358,
      "longitude": 85.32368560261718,
      "sequence": 0,
      "lat": 27.680528680951358,
      "lng": 85.32368560261718
    },
    {
      "id": 18,
      "name": "Shrestha - Jung",
      "latitude": 27.69170270565424,
      "longitude": 85.3155649454502,
      "sequence": 0,
      "lat": 27.69170270565424,
      "lng": 85.3155649454502
    },
    {
      "id": 19,
      "name": "Maharjan Ltd",
      "latitude": 27.69689460866066,
      "longitude": 85.34219874554468,
      "sequence": 0,
      "lat": 27.69689460866066,
      "lng": 85.34219874554468
    },
    {
      "id": 20,
      "name": "Kafle, Baral and Basynat",
      "latitude": 27.69249164163872,
      "longitude": 85.33017395989891,
      "sequence": 0,
      "lat": 27.69249164163872,
      "lng": 85.33017395989891
    },
    {
      "id": 21,
      "name": "Niroula, Basynat and Thapa",
      "latitude": 27.706699865937157,
      "longitude": 85.32824803549654,
      "sequence": 0,
      "lat": 27.706699865937157,
      "lng": 85.32824803549654
    },
    {
      "id": 22,
      "name": "Magar - Sherpa",
      "latitude": 27.68499640778519,
      "longitude": 85.3311833110298,
      "sequence": 0,
      "lat": 27.68499640778519,
      "lng": 85.3311833110298
    },
    {
      "id": 23,
      "name": "Dongol, Raut and Gurung",
      "latitude": 27.691099135275476,
      "longitude": 85.33298043438053,
      "sequence": 0,
      "lat": 27.691099135275476,
      "lng": 85.33298043438053
    },
    {
      "id": 24,
      "name": "Basynat, Ghale and Adhikari",
      "latitude": 27.681227532511436,
      "longitude": 85.32928212859302,
      "sequence": 0,
      "lat": 27.681227532511436,
      "lng": 85.32928212859302
    },
    {
      "id": 25,
      "name": "Rana Pvt Ltd",
      "latitude": 27.69915562975916,
      "longitude": 85.32628658406632,
      "sequence": 0,
      "lat": 27.69915562975916,
      "lng": 85.32628658406632
    },
    {
      "id": 26,
      "name": "Lama Ltd",
      "latitude": 27.697166627848173,
      "longitude": 85.32753136082722,
      "sequence": 0,
      "lat": 27.697166627848173,
      "lng": 85.32753136082722
    },
    {
      "id": 27,
      "name": "Kafle, Gyawali and Devkota",
      "latitude": 27.69700696813413,
      "longitude": 85.33622642750214,
      "sequence": 0,
      "lat": 27.69700696813413,
      "lng": 85.33622642750214
    },
    {
      "id": 28,
      "name": "Limbu - Pradhan",
      "latitude": 27.699532045230654,
      "longitude": 85.32994735326197,
      "sequence": 0,
      "lat": 27.699532045230654,
      "lng": 85.32994735326197
    },
    {
      "id": 29,
      "name": "Chettri - Subedi",
      "latitude": 27.699796932990058,
      "longitude": 85.32560847371708,
      "sequence": 0,
      "lat": 27.699796932990058,
      "lng": 85.32560847371708
    },
    {
      "id": 30,
      "name": "Khadka Group",
      "latitude": 27.704900231704695,
      "longitude": 85.3236632964715,
      "sequence": 0,
      "lat": 27.704900231704695,
      "lng": 85.3236632964715
    },
    {
      "id": 31,
      "name": "Ghale Group",
      "latitude": 27.684701257312337,
      "longitude": 85.31326804429808,
      "sequence": 0,
      "lat": 27.684701257312337,
      "lng": 85.31326804429808
    },
    {
      "id": 32,
      "name": "Lama Ltd",
      "latitude": 27.700972711778338,
      "longitude": 85.31713074506645,
      "sequence": 0,
      "lat": 27.700972711778338,
      "lng": 85.31713074506645
    },
    {
      "id": 33,
      "name": "Dongol Pvt Ltd",
      "latitude": 27.685836111526505,
      "longitude": 85.31494874590965,
      "sequence": 0,
      "lat": 27.685836111526505,
      "lng": 85.31494874590965
    },
    {
      "id": 34,
      "name": "Raut, Bhattarai and Gurung",
      "latitude": 27.679119636810473,
      "longitude": 85.3203262351637,
      "sequence": 0,
      "lat": 27.679119636810473,
      "lng": 85.3203262351637
    },
    {
      "id": 35,
      "name": "Magar - Maharjan",
      "latitude": 27.700805992050277,
      "longitude": 85.33170122958396,
      "sequence": 0,
      "lat": 27.700805992050277,
      "lng": 85.33170122958396
    },
    {
      "id": 36,
      "name": "Baral - Gyawali",
      "latitude": 27.6867779324489,
      "longitude": 85.30904806899792,
      "sequence": 0,
      "lat": 27.6867779324489,
      "lng": 85.30904806899792
    },
    {
      "id": 37,
      "name": "Kafle - Shrestha",
      "latitude": 27.693676322564823,
      "longitude": 85.34147812204269,
      "sequence": 0,
      "lat": 27.693676322564823,
      "lng": 85.34147812204269
    },
    {
      "id": 38,
      "name": "Bhattarai, Dhakal and Raut",
      "latitude": 27.699215556077643,
      "longitude": 85.33503438099599,
      "sequence": 0,
      "lat": 27.699215556077643,
      "lng": 85.33503438099599
    },
    {
      "id": 39,
      "name": "Karki - Thapa",
      "latitude": 27.703647056349006,
      "longitude": 85.31700988960587,
      "sequence": 0,
      "lat": 27.703647056349006,
      "lng": 85.31700988960587
    },
    {
      "id": 40,
      "name": "Rana, Shrestha and Subedi",
      "latitude": 27.708011721619705,
      "longitude": 85.3131784715225,
      "sequence": 0,
      "lat": 27.708011721619705,
      "lng": 85.3131784715225
    },
    {
      "id": 41,
      "name": "Jung Group",
      "latitude": 27.702638833883974,
      "longitude": 85.32420566926483,
      "sequence": 0,
      "lat": 27.702638833883974,
      "lng": 85.32420566926483
    },
    {
      "id": 42,
      "name": "Jung, Pradhan and Gyawali",
      "latitude": 27.707601924691986,
      "longitude": 85.31201362911375,
      "sequence": 0,
      "lat": 27.707601924691986,
      "lng": 85.31201362911375
    },
    {
      "id": 43,
      "name": "Shakya - Basynat",
      "latitude": 27.681540128469962,
      "longitude": 85.31697333766712,
      "sequence": 0,
      "lat": 27.681540128469962,
      "lng": 85.31697333766712
    },
    {
      "id": 44,
      "name": "Kafle - Thapa",
      "latitude": 27.684471492693394,
      "longitude": 85.32184101394245,
      "sequence": 0,
      "lat": 27.684471492693394,
      "lng": 85.32184101394245
    },
    {
      "id": 45,
      "name": "Basnet Limited",
      "latitude": 27.684728992053877,
      "longitude": 85.31828526985738,
      "sequence": 0,
      "lat": 27.684728992053877,
      "lng": 85.31828526985738
    },
    {
      "id": 46,
      "name": "Jung - Karki",
      "latitude": 27.693580651745584,
      "longitude": 85.34182841468112,
      "sequence": 0,
      "lat": 27.693580651745584,
      "lng": 85.34182841468112
    },
    {
      "id": 47,
      "name": "Lama Limited",
      "latitude": 27.702160700428273,
      "longitude": 85.31655253718223,
      "sequence": 0,
      "lat": 27.702160700428273,
      "lng": 85.31655253718223
    },
    {
      "id": 48,
      "name": "Gyawali - Maharjan",
      "latitude": 27.71054982427886,
      "longitude": 85.32640255215468,
      "sequence": 0,
      "lat": 27.71054982427886,
      "lng": 85.32640255215468
    },
    {
      "id": 49,
      "name": "Hamal - Ghale",
      "latitude": 27.70114962873887,
      "longitude": 85.33771261798655,
      "sequence": 0,
      "lat": 27.70114962873887,
      "lng": 85.33771261798655
    },
    {
      "id": 50,
      "name": "Magar, Hamal and Aryal",
      "latitude": 27.701682502482676,
      "longitude": 85.31185390373238,
      "sequence": 0,
      "lat": 27.701682502482676,
      "lng": 85.31185390373238
    }
  ]
}"""
    return data
