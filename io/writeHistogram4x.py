##
# @brief Readout a 4x data array.

def writeHistogram4x(jsFile, currencypair, histogram):
	c_h_pair = [currencypair, histogram[1:17]]
	s = str(c_h_pair)
	jsFile.write("    " + s + ",\n")
