import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib as jb
import pandas as pd
from pydantic import BaseModel
import uvicorn


from constants import features_values, data_conf

path_model = '../../models/model.clf'
path_scaler = '../../models/scaler.save'
path_features = '../../models/features.json'
path_codes = '../../models/codes.json'

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = jb.load(path_model)
scaler = jb.load(path_scaler)

with open(path_features) as f:
    features = json.load(f)
features = features['important']
features.remove('Cell_Viability (%)')

with open(path_codes) as f:
    codes = json.load(f)
for codes_key in codes.keys():
    codes[codes_key] =  dict(zip(codes[codes_key].values(), codes[codes_key].keys()))
codes_keys = codes.keys()

data_conf_inverted = dict(zip(data_conf.values(), data_conf.keys()))


class Data(BaseModel):
    coat_functional_froup: str
    concentration: float
    shape: str
    time: float
    material: str
    cell_tissue: str
    size_in_water: float
    cell_motphology: str
    cell_age: str
    cell_line: str
    cell_type: str
    no_of_cells: float
    zeta_in_water: float
    diameter: float
    cell_source: str


@app.post('/model')
async def predict(data: Data):
    data = dict(data)
    input_features = {}
    for feature in data.keys():
        this_input = data[feature]
        this_feature = data_conf[feature]
        if this_feature in codes_keys:
            this_input = codes[this_feature][this_input]
        input_features[this_feature] = this_input

    test_X = pd.DataFrame(input_features, index=[0])

    test_X = scaler.transform(test_X)

    y_predicted = model.predict(test_X)

    answer = y_predicted[0]

    return answer


@app.get('/features')
async def get_features():
    answer = {}
    for feature in features_values.keys():
        this_key = data_conf_inverted[feature]
        answer[this_key] = features_values[feature]

    return answer


uvicorn.run(app)

