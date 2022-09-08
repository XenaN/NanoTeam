import click
import json
from typing import List

import pandas as pd
from sklearn.model_selection import train_test_split


FEATURES_PATH = "models/features.json"


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path(), nargs=2)
def prepare_dataset(input_path: str, output_path: List[str]):
    """
    Preparation datasets: split to train and test
    :param input_path: path of dataset
    :param output_path: path for saving train and test datasets
    """
    df = pd.read_csv(input_path)

    for i in df.select_dtypes(include='object').columns:
        df[i] = df[i].astype('category').cat.codes

    with open(FEATURES_PATH) as json_file:
        features = json.load(json_file)

    dataset = df[features["important"]]

    train, test = train_test_split(dataset, test_size=0.1, random_state=42)

    train.to_csv(output_path[0], index=False)
    test.to_csv(output_path[1], index=False)


if __name__ == "__main__":
    prepare_dataset()

