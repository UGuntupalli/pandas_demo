import pandas as pd 


def cleanse_dataframe(df: pd.DataFrame, axis: list = None) -> pd.DataFrame:
    """Cleanses the input dataframe by dropping rows and/or columns where all values are Constants

    :param df: dataframe that needs to be cleaned
    :param axis: whether to clean rows, columns or both, defaults to None.
    1. [0] for rows
    2. [1] for columns
    3. don't specify value for both, defaults to this case
    """
    # Check if axis has been specified
    if axis is None:
        axis = [0, 1]

    # Clean Rows
    if 0 in axis:
        df = df.dropna(axis=0, how='all')

    # Clean Columns
    if 1 in axis:
        df = df.dropna(axis=1, how='all')

    # Return
    return df