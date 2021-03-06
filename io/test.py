from read4x import read_4xfile
from score4x import find10MinGain_4xdata
from score4x import find6MinGain_4xdata
from score4x import get_4xBinarySequence
from score4x import purchase1_4xdata
from score4x import purchase2_4xdata
from score4x import score1_4xdata
from score4x import score2_4xdata
from create4x import create_4xdata
from createHistogram4x import createHistogram
from writeHistogram4x import writeHistogram4x


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

    # create  JavaScript file for display
	jsFile = open('../Data/hdata.js', 'w')
	jsFile.write("var hdata = [\n")

	for fileName in fileList:
		darray = []
		ok = read_4xfile(fileName, darray)  
		if ok:
			find10MinGain_4xdata(darray)
			find6MinGain_4xdata(darray)
			#print_4xarray(darray)
			#print(get_4xBinarySequence(darray))
			
			numPurchase = purchase1_4xdata(darray)
			numPurchase2 = purchase2_4xdata(darray)

			[win, los] = score1_4xdata(darray)
			[win2, los2] = score2_4xdata(darray)
	
			print(fileName + " numPurchase= " + str(numPurchase) + ": %wins=" + str(int(100* float(win)/float(win+los))) + " wins=" + str(win) + " losses=" + str(los))
			print(fileName + " numPurchase2= " + str(numPurchase2) + ": %wins=" + str(int(100* float(win2)/float(win2+los2))) + " wins=" + str(win2) + " losses=" + str(los2))
			print

			histogram = createHistogram(get_4xBinarySequence(darray))
			writeHistogram4x(jsFile, fileName, histogram)
		else:
			print("read_4xfile failed")

	jsFile.write("];")
	jsFile.close
