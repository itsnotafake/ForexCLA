from read4x import read_4xfile
from score4x import find10MinGain_4xdata
from score4x import get_4xBinarySequence
from score4x import purchase_4xdata
from score4x import score_4xdata
from create4x import create_4xdata


def print_4xarray(darray):
	for row in darray:
		print("timeStamp=" + str(row.timeStamp) + " close=" + str(row.close) + " tenMinGain=" + str(row.tenMinGain))

test_create = False;
test_read = True;

if test_create:
	print("Running create4x test")
	darray = create_4xdata()
	find10MinGain_4xdata(darray)

if test_read:
	print("Running read4x test")
	darray = []
	#ok = read_4xfile("eur.aud_12.23.2014", darray)  
	ok = read_4xfile("gbp.jpy_12.23.2014", darray) 
	if ok:
		print("read_4xfile passed")
		find10MinGain_4xdata(darray)
		#print_4xarray(darray)
		print(get_4xBinarySequence(darray))

		purchase_4xdata(darray)
		winLoss = score_4xdata(darray)
		print("nwins= " + str(winLoss[0]) + " nLosses=" + str(winLoss[1]))
	else:
		print("read_4xfile failed")
