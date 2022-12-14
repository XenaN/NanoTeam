import click
import json
import joblib as jb
from typing import List

import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error


@click.command()
@click.argument("input_path", type=click.Path(exists=True), nargs=3)
@click.argument("output_path", type=click.Path())
def evaluate(input_path: List[str], output_path: str):
    """
    Saving score
    :param input_path: path of current model, testset and scaler
    :param output_path: path for saving score
    """
    test_df = pd.read_csv(input_path[0])
    model = jb.load(input_path[1])

    test_y = test_df["Cell_Viability (%)"]
    test_X = test_df.drop("Cell_Viability (%)", axis=1)

    scaler = jb.load(input_path[2])
    test_X = scaler.transform(test_X)

    y_predicted = model.predict(test_X)

    score = dict(
        rmse=mean_squared_error(test_y, y_predicted, squared=False),
        mae=mean_absolute_error(test_y, y_predicted),
    )

    with open(output_path, "w") as f:
        json.dump(score, f)


if __name__ == "__main__":
    evaluate()

