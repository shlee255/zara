from pandas import read_csv
from pandas import DataFrame
from pandas import Grouper
from matplotlib import pyplot
series = read_csv('daily-min-temperatures.txt', header=0, index_col=0, parse_dates=True, squeeze=True)
groups = series.groupby(Grouper(freq='D')) # https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases
years = DataFrame()
for name, group in groups:
    print(name)
    print(group)
#	years[name.year] = group.values
#years.plot(subplots=True, legend=False)
#pyplot.show()