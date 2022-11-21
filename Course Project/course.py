import pandas as pd
import csv
import os
import numpy as np  
from numpy import nan
from matplotlib import pyplot as plt

current_path = os.getcwd()
filelist = os.listdir(current_path)
tendays_data = []
for i in filelist:
    if i.endswith("00"):
        with open(i,'r', encoding='utf-8' ) as f:
            for j in csv.reader(f):
                tendays_data.append(j)

np.unique(np.array([len(i) for i in tendays_data]))
#Since data should be 19 columns long, we have to clean the dataset first
lengthof8 = 0
lengthof20 = 0
for i in tendays_data:
    if len(i) == 8:
        lengthof8 += 1
    elif len(i) == 20:
        lengthof20 += 1
print(lengthof8,lengthof20)

clean_tendays_data = []
for i in tendays_data:
    if len(i) == 20:
        del i[-1]
        clean_tendays_data.append(i)
    elif len(i) == 8:
        i.extend([nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan])
        clean_tendays_data.append(i)

df = pd.DataFrame(clean_tendays_data,columns=['DriverID',"PlateNumber","Latitude",
                          "Longtitude","Speed","Direction",
                          "SiteName","Time","IsRapidlySpeedup",
                           "IsRapidlySlowdown","IsNeutralSlide",
                          "IsNeutralSlideFinished","NeutralSlideTime",
                          "IsOverspeed","IsOverspeedFinished",
                          "OverspeedTime","IsFatigueDriving",
                          "IsHthrottleStop","IsOilLeak"])

display(df)

df["PlateNumber"].unique()

df["DriverID"].unique()

for i in df:
    df[i] = df[i].replace(nan,0)
    df[i] = df[i].replace("",0)

for i in  ['DriverID',"PlateNumber","Latitude",
                          "Longtitude","Speed","Direction",
                          "SiteName","Time"]:
    df[i] = df[i].replace(0,nan)
display(df)

df["Time"][1][:10]

df["Date"] = [i[:10] for i in df.Time]
df["Time_detail"] = [i[11:] for i in df.Time]
df.Date.unique()

df["IsOverspeed"] = pd.to_numeric(df.IsOverspeed, downcast="integer")
df["IsFatigueDriving"] = pd.to_numeric(df.IsFatigueDriving, downcast="integer")
df["NeutralSlideTime"] = pd.to_numeric(df.NeutralSlideTime, downcast="integer")
df["OverspeedTime"] = pd.to_numeric(df.OverspeedTime, downcast="integer")

df.groupby(["Date","PlateNumber"])["IsOverspeed","IsFatigueDriving","NeutralSlideTime","OverspeedTime"].sum()

behavior_stat = df.groupby(["Date","PlateNumber"])["IsOverspeed","IsFatigueDriving","NeutralSlideTime","OverspeedTime"].sum()
behavior_stat.to_csv("behavior statistics",index = True)

df.Time = pd.to_datetime(df.Time,format = "%Y-%m-%d %H:%M:%S")
df["Speed"] = pd.to_numeric(df.Speed, downcast="integer")
df["Hour"] = pd.to_datetime(df.Time.astype(str)).dt.hour
df["Date"] = pd.to_datetime(df.Date,format = "%Y-%m-%d").dt.normalize()

group_data = df.groupby("Date")["Speed","Hour","PlateNumber"]

for i in ["2017-01-01","2017-01-02","2017-01-03",
         "2017-01-04","2017-01-05","2017-01-06",
         "2017-01-07","2017-01-08","2017-01-09",
         "2017-01-10","2017-01-11"]:
    one_day_data = group_data.get_group(i).groupby(["Hour","PlateNumber"]).agg(Speed=('Speed', 'mean')).reset_index()
    fig, ax = plt.subplots(figsize=(10,5))
    one_day_data.set_index('Hour', inplace=True)
    one_day_data.groupby('PlateNumber')['Speed'].plot(legend=True,title=i)

import statsmodels.api as sm
import statsmodels.formula.api as smf

df["Direction"] = pd.to_numeric(df.Direction, downcast="integer")
df["IsRapidlySpeedup"] = pd.to_numeric(df.IsRapidlySpeedup, downcast="integer")
df["IsRapidlySlowdown"] = pd.to_numeric(df.IsRapidlySlowdown, downcast="integer")
df["IsNeutralSlide"] = pd.to_numeric(df.IsNeutralSlide, downcast="integer")
df["IsNeutralSlideFinished"] = pd.to_numeric(df.IsNeutralSlideFinished, downcast="integer")
df["NeutralSlideTime"] = pd.to_numeric(df.NeutralSlideTime, downcast="integer")
df["IsOverspeed"] = pd.to_numeric(df.IsOverspeed, downcast="integer")
df["IsOverspeedFinished"] = pd.to_numeric(df.IsOverspeedFinished, downcast="integer")
df["OverspeedTime"] = pd.to_numeric(df.OverspeedTime, downcast="integer")
df["IsHthrottleStop"] = pd.to_numeric(df.IsHthrottleStop, downcast="integer")
df["IsOilLeak"] = pd.to_numeric(df.IsOilLeak, downcast="integer")

reg_1 = smf.ols("IsFatigueDriving~Speed+Direction+IsRapidlySpeedup+IsRapidlySlowdown+IsNeutralSlide+IsNeutralSlideFinished+IsOverspeedFinished+IsOverspeed+OverspeedTime+IsHthrottleStop+IsOilLeak+Hour",data =df).fit()

print(reg_1.summary())

