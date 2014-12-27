##
# @brief Read a 4x data file.
#
# @param fileName The name of a .csv file.
# @param darray An empty array.
# @return True or False
#
# @author itsnotafake
#
# Reads a .csv file from the Data folder and allocates
# FxEntry objects, one per line.

import csv
import datetime
import time

from FxEntry import FxEntry

def read_4xfile(fileName, darray):
   
    lineNumber = 0
    with open("../Data/" + fileName + ".csv", 'rb') as csvfile:
		fxreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for fxLine in fxreader:
			if(lineNumber > 0):
							
				dt = datetime.datetime.strptime(fxLine[0], "%m/%d/%Y %H:%M:%S %p")	
				
				entry = FxEntry()
				entry.dateString = fxLine[0]
				entry.timeStamp = int(time.mktime(dt.timetuple()))
				entry.open  = float(fxLine[1])
				entry.high  = float(fxLine[2])
				entry.low   = float(fxLine[3])
				entry.close = float(fxLine[4])

				darray.append(entry)
			lineNumber += 1
	
    return True