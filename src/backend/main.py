from this import s
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import joblib as jb
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

from pydantic import BaseModel

from typing import List

# from data_request_model import *

path_model = './model.clf'

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Data(BaseModel):
  material: str
  hydro_size: str
  cell_line: str
  time: str
  dose: str

model = jb.load(path_model)

@app.post('/model')
async def predict(data: Data):
    enc = OneHotEncoder()
    df = pd.read_csv('toxic.csv')
    df = df.drop('viability', axis=1)
    enc_data = pd.DataFrame(enc.fit_transform(df[["material", "cell_line"]]).toarray())

    new_df = df.join(enc_data)
    dataset = pd.get_dummies(new_df, columns=["material", "cell_line"])

    # material = 'CuO'
    # hydro_size = 257.0
    # cell_line = 'A549'
    # time = 80
    # dose = 100.0
    data = {'material': [data.material], 'hydro_size': [float(data.hydro_size)], 
      'cell_line': [data.cell_line], 'time': [float(data.time)], 'dose': [float(data.dose)]}

    df_new = pd.DataFrame(data, index=[13])
    df = df.append(df_new)

    enc_data = pd.DataFrame(enc.fit_transform(df[["material", "cell_line"]]).toarray())

    new_df = df.join(enc_data)
    dataset = pd.get_dummies(new_df, columns=["material", "cell_line"])

    y_predicted = model.predict(dataset)

    answer = y_predicted[-1]

    return answer

from constants import features
@app.get('/features')
async def get_features():
  return features


import uvicorn
uvicorn.run(app)


{
  "material": "CuO",
  "hydro_size": "257.0",
  "cell_line": "A549",
  "time": "80",
  "dose": "100.0"
}