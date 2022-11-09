datas = []
drivers = {}

def overview(filename):
	with open(filename)  as csvfile:
		lines = csvfile.read().splitlines()

	for line in lines:
		datas.append(line.split(","))

	for data in datas:
		if data[0] in drivers:
			drivers[data[0]] = drivers[data[0]] + 1
		else:
			drivers[data[0]] = 1

	print(drivers)
	print(filename)
	print("Number of Records: " + str(len(lines)) + ", Number of Drivers: " + str(len(drivers)))

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
