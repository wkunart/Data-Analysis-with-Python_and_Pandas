import numpy as np
import pandas as pd
df1 = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))

print(df1)


#df.to_csv("bigfile.csv")
