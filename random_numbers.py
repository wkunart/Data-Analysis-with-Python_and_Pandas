import numpy as np
import pandas as pd

data = np.random.randint(5,30,size=(10,3))
df_int = pd.DataFrame(data, columns=['random_col_1', 'random_col_2', 'random_col_3'])

print(df_int)
