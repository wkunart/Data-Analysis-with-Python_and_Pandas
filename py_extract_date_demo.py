import pandas as pd
import numpy as np
dates = pd.date_range("2018-02-01", periods=40, freq="d")

df=pd.DataFrame({"date_col":dates})

print("#################################################")
print(df["date_col"].dtypes)

df["day_new"]=df["date_col"].dt.day
df["week_new"]=df["date_col"].dt.isocalendar().week
df["month_new"]=df["date_col"].dt.month
df["quarter_new"]=df["date_col"].dt.quarter
df["half_year_new"]=np.where(df["date_col"].dt.quarter<3,"1","2")
df["year_new"]=df["date_col"].dt.year

df["dayofyear_new"]=df["date_col"].dt.dayofyear
df["dayofweek_new"]=df["date_col"].dt.dayofweek
df["days_in_month_new"]=df["date_col"].dt.days_in_month

print(df)
print("#################################################")
print(pd.DataFrame({"all_columns":df.columns}))
print("#################################################")

