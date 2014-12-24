from read4x import read_4xfile
from score4x import score_4xdata
from create4x import create_4xdata

test_create = True;
test_read = False;

if test_create:
	print("Running create4x test")
	darray = create_4xdata()
	score_4xdata(darray)

if test_read:
	print("Running read4x test")
	darray = []
	ok = read_4xfile("abc", darray)
	if ok:
		print("read_4xfile passed")
		score_4xdata(darray)
	else:
		print("read_4xfile failed")
