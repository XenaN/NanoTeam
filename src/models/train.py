import click
import joblib as jb
import json
from typing import List

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler


HYPERPARAMETERS_PATH = "models/parameters.json"


@click.command()
@click.argument("input_path", type=click.Path(exists=True), nargs=2)
@click.argument("output_path", type=click.Path(), nargs=2)
def train(input_path: List[str], output_path: List[str]):
    """
    Train model
    :param input_path: path of train and test datasets
    :param output_path: path for saving model, path to scaler
    """
    train_df = pd.read_csv(input_path[0])
    test_df = pd.read_csv(input_path[1])
    assert isinstance(train_df, pd.DataFrame)
    assert isinstance(test_df, pd.DataFrame)

    with open(HYPERPARAMETERS_PATH) as json_file:
        parameters = json.load(json_file)

    train_y = train_df["Cell_Viability (%)"]
    train_X = train_df.drop("Cell_Viability (%)", axis=1)

    scaler = StandardScaler()
    scaler.fit(train_X)
    train_X = scaler.transform(train_X)

    jb.dump(scaler, output_path[1])

    model = RandomForestRegressor(random_state=42, **parameters)

    model.fit(train_X, train_y)

    jb.dump(model, output_path[0])


if __name__ == "__main__":
    train()

