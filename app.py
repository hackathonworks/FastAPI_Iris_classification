# 1. Library imports
import uvicorn
from fastapi import FastAPI
from iris import iris
#import numpy as np
import pickle
#import pandas as pd
# 2. Create the app object
some_file_path='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Iris_pallida_Variegata_1zz.jpg/800px-Iris_pallida_Variegata_1zz.jpg'
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.post('/predict')
def predict_results(data:iris):
    data = data.dict()
    sepal_length=data['sepal_length']
    sepal_width=data['sepal_width']
    petal_length=data['petal_length']
    petal_width=data['petal_width']
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    result='The Variant is iris '+prediction[0]
    return {
        'prediction': result
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload