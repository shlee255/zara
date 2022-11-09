import pandas as pd
import matplotlib.pyplot as plt

# https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html

def overview(filename):
	df = pd.read_csv(filename,header = None, names=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] )
	#print(df)
	df[5].plot()
	plt.show()

overview('COMP1012-Project-data/driving-records/detail_record_2017_01_02_08_00_00')
overview('COMP1012-Project-data/driving-records/detail_record_2017_01_03_08_00_00')
overview('COMP1012-Project-data/driving-records/detail_record_2017_01_04_08_00_00')
overview('COMP1012-Project-data/driving-records/detail_record_2017_01_05_08_00_00')
overview('COMP1012-Project-data/driving-records/detail_record_2017_01_06_08_00_00')
overview('COMP1012-Project-data/driving-records/detail_record_2017_01_07_08_00_00')
overview('COMP1012-Project-data/driving-records/detail_record_2017_01_08_08_00_00')
overview('COMP1012-Project-data/driving-records/detail_record_2017_01_09_08_00_00')
overview('COMP1012-Project-data/driving-records/detail_record_2017_01_10_08_00_00')
overview('COMP1012-Project-data/driving-records/detail_record_2017_01_11_08_00_00')
