import pandas as pd
import numpy as np


np.random.seed(10)

date_range =  pd.date_range(start='1/1/2000 06:30', periods=500000, freq="Min")

time=np.random.choice(['foo','bar','baz'], size=(500000,1))

df=pd.DataFrame({"date_info":date_range}, time)



print(df.head(50))


#df.to_csv("bigfile.csv")
