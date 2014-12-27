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

from FxEntry import FxEntry

def read_4xfile(fileName, darray):
    print("reading: " + "../Data/" + fileName + ".csv")

    lineNumber = 0
    with open("../Data/" + fileName + ".csv", 'rb') as csvfile:
		fxreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for fileLine in fxreader:
			if(lineNumber > 0):
				entry = FxEntry()
				entry.dateString = fileLine[0]

				dt = datetime.datetime.strptime(entry.dateString, "%m/%d/%Y %H:%M:%S %p")	
				entry.timeStamp = int(time.mktime(dt.timetuple()))

				entry.open = float(fileLine[1])
				entry.high = float(fileLine[2])
				entry.low = float(fileLine[3])
				entry.close = float(fileLine[4])

				darray.append(entry)
			lineNumber += 1
	
    return True