import pandas as pd
import matplotlib.pyplot as plt
import datetime

# https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html

def overview(filename):
	df = pd.read_csv(filename,header = None, names=[
			"driverID",
			"carPlateNumber",
			"Latitude",
			"Longtitude",
			"Speed",
			"Direction",
			"siteName",
			"Time",
			"isRapidlySpeedup",
			"isRapidlySlowdown",
			"isNeutralSlide",
            "isNeutralSlideFinished",
			"neutralSlideTime",
            "isOverspeed",
			"isOverspeedFinished",
            "overspeedTime",
			"isFatigueDriving",
            "isHthrottleStop",
			"isOilLeak",
			"other"]).fillna(value = 0)

	print("There are " + str(len(df.driverID)) + " records and " + str(len(df.driverID.unique())) + " drivers in " + filename)
	#print(df)
	#df[5].plot()
	#plt.show()
	return df
frames = [
	overview('COMP1012-Project-data/driving-records/detail_record_2017_01_02_08_00_00'),
	overview('COMP1012-Project-data/driving-records/detail_record_2017_01_03_08_00_00'),
	overview('COMP1012-Project-data/driving-records/detail_record_2017_01_04_08_00_00'),
	overview('COMP1012-Project-data/driving-records/detail_record_2017_01_05_08_00_00'),
	overview('COMP1012-Project-data/driving-records/detail_record_2017_01_06_08_00_00'),
	overview('COMP1012-Project-data/driving-records/detail_record_2017_01_07_08_00_00'),
	overview('COMP1012-Project-data/driving-records/detail_record_2017_01_08_08_00_00'),
	overview('COMP1012-Project-data/driving-records/detail_record_2017_01_09_08_00_00'),
	overview('COMP1012-Project-data/driving-records/detail_record_2017_01_10_08_00_00'),
	overview('COMP1012-Project-data/driving-records/detail_record_2017_01_11_08_00_00')]

dataset = pd.concat(frames)

print("There are " + str(len(dataset.driverID)) + " records and " + str(len(dataset.driverID.unique())) + " drivers")

print(dataset)

# speedAnalytics = dataset.groupby("Time")["Speed","carPlateNumber"].agg(Speed=('Speed', 'mean')).reset_index()

# fig, ax = plt.subplots(figsize=(10,5))

# speedAnalytics.set_index('Time', inplace=True)

print(dataset['Time'].dtypes)

dataset['Datetime'] = pd.to_datetime(dataset['Time'])
dataset.set_index('Datetime')
dataset.groupby('driverID')[['Speed']].plot(legend=True,title="Speed")

#print(dataset['Datetime'].dtypes)
#print(dataset.values.tolist())
#print(dataset.groupby(['driverID'])[['Datetime','Speed']].values.tolist())
#plt.plot()
plt.show()
