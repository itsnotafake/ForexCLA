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

def find6MinGain_4xdata(darray):
	for i in range(0, len(darray) -3):
		entry1 = darray[i]
		entry2 = darray[i+3]

		#True - the closing price went up or stayed the same at the end of 6 minutes
		#False - the closing price went down at the end of 6 minutes

		entry1.sixMinGain = (entry2.close >= entry1.close)

		#print ("i= " + str(i) + ", close1 = " + str(entry1.close) + ", close2 = " + str(entry2.close) + ", sixMinGain = " + str(entry1.sixMinGain))


def get_4xBinarySequence(darray):
	binarySequence = ""
	for entry in darray:
		if(entry.tenMinGain == True):
			binarySequence += "1"
		elif(entry.tenMinGain == False):
			binarySequence += "0"

	return binarySequence

def purchase1_4xdata(darray):
	numPurchase = 0
	for i in range (5, len(darray)):
		oldEntry = darray[i-5]
		curEntry = darray[i]
		if(oldEntry.tenMinGain):
			curEntry.purchaseCall_10min = True;
			numPurchase += 1
			
	return numPurchase

def purchase2_4xdata(darray):
	numPurchase = 0
	for i in range(3, len(darray)):
		oldEntry = darray[i-3]
		curEntry = darray[i]
		if(oldEntry.sixMinGain):
			curEntry.purchaseCall_6min = True;
			numPurchase += 1

	return numPurchase

def score1_4xdata(darray):
	win = 0
	los = 0
	for entry in darray:
		if(entry.purchaseCall_10min):
			if(entry.tenMinGain):
				win += 1
			else:
				los += 1
	
	return [win, los]

def score2_4xdata(darray):
	win = 0
	los = 0
	for entry in darray:
		if(entry.purchaseCall_6min):
			if(entry.sixMinGain):
				win += 1
			else:
				los += 1
	
	return [win, los]