import pandas as pd
import numpy as np
data = {"X1": [np.nan, "Red" , "Blue", "Red", np.nan,
        "Red", "Green", np.nan, "Blue", "Red"],
        "X2": ["Green", "Green", "Red", "Blue", "Green" ,
        "Blue" , np.nan, "Red", "Green", np.nan ]}
df = pd.DataFrame(data, columns = ['X1', 'X2'])
print(df)