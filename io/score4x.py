##
# @brief Score a 4x data array.
#
# @param darray A 4x data array.
#
# @author
#
# Iterates over a 4x data array and adds a score element for each entry:
#  0 - the closing price went down at the end of 10 minutes
#  1 - the closing price went up or stayed the same at the end of 10 minutes
def score_4xdata(darray):
	data_array_length = len(darray)
	print (data_array_length)
	for x in range (0, data_array_length - 5):
		row1 = darray[x]
		row2 = darray[x+5]
		if(row2[4] < row1[4]):
			row1[5] = 0
		else:
			row1[5] = 1 
		print ("x= " + str(x) + ", close1 = " + str(row1[4]) + ", close2 = " + str(row2[4]) + ", score1 = " + str(row1[5]))

