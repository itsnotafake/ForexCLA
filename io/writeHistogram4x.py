##
# @brief Readout a 4x data array.

def readout4x(currencypair,histogram):
	c_h_pair = [currencypair, histogram]
	s = str(c_h_pair)

	f = open('hdata.js', 'a')
	f.write(s)
	f.close

