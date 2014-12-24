from read4x import read_4xfile
from score4x import score_4xdata

darray = []
ok = read_4xfile("abc", darray)
if ok:
	print("read_4xfile passed")
	score_4xdata(darray)
else:
	print("read_4xfile failed")
