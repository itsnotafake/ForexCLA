##
# @brief Calculate gain after 10 minutes.
#
# @param darray A 4x data array.
#
# @author
#
# Iterates over a 4x data array and check wheter closing price rises in 10 minutes.

def find10MinGain_4xdata(darray):
	for i in range (0, len(darray) - 5):
		entry1 = darray[i]
		entry2 = darray[i+5]

		#  True  - the closing price went up or stayed the same at the end of 10 minutes
		#  False - the closing price went down at the end of 10 minutes

		entry1.tenMinGain = (entry2.close >= entry1.close)

		#print ("i= " + str(i) + ", close1 = " + str(entry1.close) + ", close2 = " + str(entry2.close) + ", tenMinGain = " + str(entry1.tenMinGain))


def get_4xBinarySequence(darray):
	binarySequence = ""
	for entry in darray:
		if(entry.tenMinGain == True):
			binarySequence += "1"
		elif(entry.tenMinGain == False):
			binarySequence += "0"

	return binarySequence

def purchase_4xdata(darray):
	numPurchase = 0
	for i in range (5, len(darray)):
		oldEntry = darray[i-5]
		curEntry = darray[i]
		if(oldEntry.tenMinGain):
			curEntry.purchaseCall = True;
			numPurchase += 1
			
	return numPurchase

def score_4xdata(darray):
	win = 0
	los = 0
	for entry in darray:
		if(entry.purchaseCall):
			if(entry.tenMinGain):
				win += 1
			else:
				los += 1
	
	return [win, los]