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

    for i in df.select_dtypes(include='object').columns:
        df[i] = df[i].astype('category').cat.codes

    n_train = int(df.shape[0]*0.9)
    train, test = df.iloc[:n_train], df.iloc[n_train:]

    train.to_csv(output_path[0], index=False)
    test.to_csv(output_path[1], index=False)


if __name__ == "__main__":
    prepare_dataset()

