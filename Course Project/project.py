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
			"other"]) #,
            # index_col="Time", parse_dates=True)#.fillna(value = 0)

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
dataset.to_csv('dataset.csv')

dataset["Date"] = [i[:10] for i in dataset.Time]

behavior = dataset.groupby(["Date","carPlateNumber"])[["isOverspeed","isFatigueDriving","neutralSlideTime","overspeedTime"]].sum()

print(behavior)
behavior.to_csv('behavior.csv')

# Plot Driver vs Speed
speedData = dataset[["Time", "driverID", "Speed"]]
speedData = speedData.drop_duplicates(["Time","driverID"])
speedData['Time'] = pd.to_datetime(speedData['Time'], format='%Y-%m-%d %H:%M:%S') # 2017-01-01 08:00:20
speedData = speedData.set_index("Time")
print(speedData)

speed_pivot = speedData.pivot(columns='driverID',values='Speed')
print(speed_pivot)

speed_pivot.to_csv('speed.csv')

speed_pivot.plot(figsize=(10,5),subplots=True,ylabel="Speed",marker='.') # ,linestyle='none')

plt.show()






