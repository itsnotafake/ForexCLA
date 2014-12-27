#this function will create a histogram depicting the various run lengths of 0's and 1's
def createHistogram(binarysequence): #this takes in binarysequence
	histogram_array = [0]*100

	binarysequence_array = binarysequence

	counter = 0 #keeps track of consecutive run in binary sequence
	current = None

	for i in range(len(binarysequence)):
		if current != binarysequence[i]:
			current = binarysequence[i]
			histogram_array[counter] = histogram_array[counter] + 1
			counter = 1
		else:
			counter += 1

	print histogram_array
