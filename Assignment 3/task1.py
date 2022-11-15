#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime # , timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

counting = pd.read_csv("counting.csv", index_col=0,parse_dates=True)

# https://numpy.org/doc/stable/reference/generated/numpy.interp.html

#counting.plot()
# plt.show()

print(counting)

# counting = pd.concat([counting, pd.DataFrame(["2022-09-02 00:02:30",1],columns=counting.columns)])
#print(counting)

#df = df.append({'a': 1, 'b': 2}, ignore_index=True)

#df = pd.DataFrame(["2022-09-02 00:02:30"], columns=["Time"])
#df = pd.concat([pd.DataFrame([[1,2]], columns=df.columns), df], ignore_index=True)

# print(df)

counts = counting["Counts"]


print(counting)

# print(counting)
# print(counting[counting["Counts"]>0])


# air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)


starttime = datetime.datetime(2022, 9, 2) + datetime.timedelta(seconds = 150)
ndays = 288
df = pd.DataFrame({'date': [starttime + datetime.timedelta(seconds=x*300) for x in range(ndays)], 
                   'Counts': None})
df = df.set_index('date')

print(df)

result = pd.concat([counting,df])

result.sort_values()
print( result)
result.to_csv('results_T1.csv')
