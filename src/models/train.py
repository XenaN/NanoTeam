import click
import joblib as jb
from typing import List

import pandas as pd
from sklearn.ensemble import RandomForestRegressor


@click.command()
@click.argument("input_path", type=click.Path(exists=True), nargs=2)
@click.argument("output_path", type=click.Path())
def train(input_path: List[str], output_path: str):
    """
    Find the best hyperparameters, train model and tracking experiment by mlflow
    :param input_path: path of train and test datasets
    :param output_path: path for saving model
    """
    train_df = pd.read_csv(input_path[0])
    test_df = pd.read_csv(input_path[1])
    assert isinstance(train_df, pd.DataFrame)
    assert isinstance(test_df, pd.DataFrame)

    train_y = train_df["viability"]
    train_X = train_df.drop("viability", axis=1)

    model = RandomForestRegressor(random_state=0)

    model.fit(train_X, train_y)

    jb.dump(model, output_path)


if __name__ == "__main__":
    train()

