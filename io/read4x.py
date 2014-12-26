##
# @brief Read a 4x data file.
#
# @param fileName The name of a .csv file.
# @param darray An empty array.
# @return True or False
#
# @itsnotafake
#
# Reads a .csv file from the Data folder and allocates
# array elements, one per line. Each element is an
# array with format [tstamp, open, high, low, close, None]

import csv
import datetime
import time

def read_4xfile(fileName, darray):
    print("reading: " + "../Data/" + fileName + ".csv")

    rowNumber = 0
    with open("../Data/" + fileName + ".csv", 'rb') as csvfile:
		fxreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for fileRow in fxreader:
			if(rowNumber > 0):
				dateString = fileRow[0]
				dt = datetime.datetime.strptime(dateString, "%m/%d/%Y %H:%M:%S %p")
				
				timestamp = time.mktime(dt.timetuple())

				dataRow = [
					int(timestamp), float(fileRow[1]), float(fileRow[2]), float(fileRow[3]), float(fileRow[4]), None
				]
				darray.append(dataRow)
			rowNumber += 1
	
    return True