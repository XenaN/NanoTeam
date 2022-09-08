import click
from typing import List

import numpy as np
import pandas as pd


def removal_outliers(data: pd.DataFrame,
                     columns: list,
                     min_q: float,
                     max_q: float) -> pd.DataFrame:
    """
    Function for remove outliers
    :param data: you data
    :param columns: columns with outliers
    :param min_q: Q1 percentile values
    :param max_q: Q3 percentile values
    :return: list of name features to drop
    """
    df = data.copy()

    for i, col in enumerate(columns):
        Q1 = df[col].quantile(min_q)
        Q3 = df[col].quantile(max_q)

        df[col] = df[(df[col] > Q1) & (df[col] < Q3)][col]

    df.dropna(inplace=True)

    return df


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
    data.drop(["Year",
               "Size_in_Medium (nm)",
               "Zeta_in_Medium (mV)",
               "Aspect_Ratio",
               "PDI",
               "DOI",
               "Article_ID"], axis=1, inplace=True)
    data.dropna(inplace=True)
    data["Zeta_in_Water (mV)"] = data["Zeta_in_Water (mV)"].astype('float32')
    columns_to_clean = ["Diameter (nm)", "No_of_Cells (cells/well)", "Concentration (ug/ml)"]

    data = removal_outliers(data, columns_to_clean, 0, 0.99)

    data["Cell_Viability (%)"] = abs(data["Cell_Viability (%)"])
    data[data["Cell_Viability (%)"] > 100] = 100

    data.to_csv(output_path, index=False)


if __name__ == "__main__":
    clean()

