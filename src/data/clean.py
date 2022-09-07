import click
from typing import List

import numpy as np
import pandas as pd


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path())
def clean(input_path: str, output_path: str):
    """
    Cleaning dataset
    :param input_path: path of raw dataset
    :param output_path: path of clean dataset
    """
    data = pd.read_excel(input_path)
    data.drop(['Year',
               'Size_in_Medium (nm)',
               'Zeta_in_Medium (mV)',
               'Aspect_Ratio',
               'PDI',
               'DOI',
               'Article_ID'], axis=1, inplace=True)
    data.dropna(inplace=True)

    data.to_csv(output_path, index=False)


if __name__ == "__main__":
    clean()