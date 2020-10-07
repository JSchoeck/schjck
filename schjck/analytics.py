import pandas as pd
from typing import Dict

def count_missing(df: pd.DataFrame) -> Dict[str, int]:
    return dict(df.isna().sum())