# Functions to write
#    Plot distributions for all columns/features
#    Outlier detection for various datatypes (categoric, numeric, timestamps etc.)
#    Missing values detection and handling

import pandas as pd
from typing import Dict

def count_missing(df: pd.DataFrame) -> Dict[str, int]:
    return dict(df.isna().sum())