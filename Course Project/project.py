with open('COMP1012-Project-data/driving-records/detail_record_2017_01_02_08_00_00')  as csvfile:
	lines = csvfile.read().splitlines()

#for line in lines:
#	print(line)

print("Number of Tecords: " + str(len(lines)))