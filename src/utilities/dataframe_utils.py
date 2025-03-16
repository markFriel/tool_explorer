from typing import List

import numpy as np
import pandas as pd


def split_df_into_even_chunks(df: pd.DataFrame, number_of_chunks: int) -> List[pd.DataFrame]:
    """
    Splits a Dataframe into a number of evenly sized chunks as possible, odd number of records will result in a dataframe
    that is of different length than the rest. This is usefull for passing a dataframe into a multi-processing function

    args:
        df: a pandas dataframe
        number_of_chunks: the number of chunks to split the dataframe into

    return:
        chunks a list of Dataframes
    """

    chunks = np.array_split(df, number_of_chunks)
    return chunks
