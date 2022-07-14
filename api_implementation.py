# -*- coding: utf-8 -*-
"""
@author: Vaishali Ravindranath
"""


import json
import requests


url = 'http://127.0.0.1:8000/predict'

input_data_for_model = {
  "sepal_length": 5.1,
  "sepal_width": 2.2,
  "petal_length": 4,
  "petal_width": 1
}

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)




