# FastAPI
#api_implementation.py 


#iris classification with random forest

#Step 1: download the code


#step 2: Open app.py


#Step 3: open conda prompt and type activate myenv


#step 4: type cd <working directory> in the conda prompt


#step 5: type uvicorn app:app --reload
  
# app gets hosted in http://127.0.0.1:8000/docs 


################# api_implementation.py ####################

# To do get and post from the server. Use the following code




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



