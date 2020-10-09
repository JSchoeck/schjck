import pandas as pd
import numpy as np

cities = pd.DataFrame(
data={
    "city": [
        "Berlin",
        "Vienna",
        "Montreal",
        "Mumbai",
        "cape-town",
        "Cape Town",
        "Sydney",
    ],
    "country": ["DE", "AT", "CA", "IN", np.nan, "ZA", "AUS"],
    "population": [3750000, 1900000, 1780000, 184100000, 430000, 440000, np.nan],
}
)
"""Provides simple dataframe with missing and oulier data point.
"""