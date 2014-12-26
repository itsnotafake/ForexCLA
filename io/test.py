from read4x import read_4xfile
from score4x import score_4xdata
from create4x import create_4xdata


def print_4xarray(darray):
	for row in darray:
		print("tstamp=" + str(row[0]) + " close=" + str(row[4]) + " score=" + str(row[5]))

test_create = False;
test_read = True;

if test_create:
	print("Running create4x test")
	darray = create_4xdata()
	score_4xdata(darray)

if test_read:
	print("Running read4x test")
	darray = []
	ok = read_4xfile("eur.aud_12.23.2014", darray)
	if ok:
		print("read_4xfile passed")
		score_4xdata(darray)
		print_4xarray(darray)
	else:
		print("read_4xfile failed")
