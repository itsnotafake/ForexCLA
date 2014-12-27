class FxEntry:
	dateString = ""
	timeStamp = 0	# in seconds
	open = 0.0
	high = 0.0
	low = 0.0
	close = 0.0

	#  0 - the closing price went down at the end of 10 minutes
	#  1 - the closing price went up or stayed the same at the end of 10 minutes
	tenMinGain = None

	# True we are making a call purchase
	# False we are making a put purchase
	# None we are making no purchase
	purchaseCall = None
