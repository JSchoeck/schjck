# Functions to write
#    Outlier detection for various datatypes (categoric, numeric, timestamps etc.)
#    Missing values detection and handling
#    Correlation matrix (or better, see articles)
#    
#    
#    https://www.analyticsvidhya.com/blog/2020/10/a-quick-guide-to-descriptive-statistics-the-first-step-in-exploring-your-data
#    

import pandas as pd
from typing import Dict

def count_missing(df: pd.DataFrame) -> Dict[str, int]:
    return dict(df.isna().sum())