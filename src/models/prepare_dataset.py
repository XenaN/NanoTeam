import click
from typing import List

import pandas as pd


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

    dataset = pd.get_dummies(df, columns=["material", "cell_line"])

    n_train = int(dataset.shape[0] - 1)
    train, test = dataset.iloc[:n_train], dataset.iloc[n_train:]

    train.to_csv(output_path[0], index=False)
    test.to_csv(output_path[1], index=False)


if __name__ == "__main__":
    prepare_dataset()

