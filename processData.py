import os
import pexpect

def getFileList(directoryName):
	files = os.listdir(directoryName)
	files = list(filter(lambda s: ".lm" in s, files))

	return files

def ctrack(dirname, filename, fopt=50, N=250):
	child = pexpect.spawn(dirname + "ctrack")
	child.sendline(dirname + "/" + filename)
	print(child.readline())

	child.sendline("") # First Event
	print(child.readline())

	child.sendline("") # Last Event
	print(child.readline())

	child.sendline(str(N)) # Events/Slice
	print(child.readline())

	child.sendline("") # Locations/Slice
	print(child.readline())

	child.sendline(str(fopt)) # Fopt
	print(child.readline())

	child.sendline("") # Max allowable error
	print(child.readline())

	child.sendline("A") # Output ASCII/Binary
	print(child.readline())
	print(child.readline())
	#print(child.readline())

ctrack("../RawData/","cal_10")
#print(getFileList("../RawData/"))