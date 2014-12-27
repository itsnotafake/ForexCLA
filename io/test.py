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

	fileList = ["eur.aud_12.23.2014", "eur.usd_12.23.2014", "gbp.jpy_12.23.2014", "gbp.usd_12.23.2014", "usd.cad_12.23.2014", "usd.jpy_12.23.2014"]
	#fileList = ["eur.usd_12.23.2014"]

	for fileName in fileList:
		darray = []
		ok = read_4xfile(fileName, darray)  
		if ok:
			find10MinGain_4xdata(darray)
			#print_4xarray(darray)
			#print(get_4xBinarySequence(darray))

			numPurchase = purchase_4xdata(darray)
			[win, los] = score_4xdata(darray)
	
			print(fileName + " numPurchase= " + str(numPurchase) + ": %wins=" + str(int(100* float(win)/float(win+los))) + " wins=" + str(win) + " losses=" + str(los))
		else:
			print("read_4xfile failed")
