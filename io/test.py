from read4x import read_4xfile

ok = read_4xfile("abc", [])
if ok:
	print("read_4xfile passed")
else:
	print("read_4xfile failed")
