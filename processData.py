import os
import pexpect

def getFileList(directoryName):
	files = os.listdir(directoryName)
	files = list(filter(lambda s: ".lm" in s, files))
	files = list(map(lambda s: s[:-5], files))

	return files

def ctrack(dirname, filename, fopt=50, N=250):
	child = pexpect.spawn(dirname + "ctrack", timeout=999999)

	child.sendline(dirname + "/" + filename)
	child.sendline("") # First Event
	child.sendline("") # Last Event
	child.sendline(str(N)) # Events/Slice
	child.sendline("") # Locations/Slice
	child.sendline(str(fopt)) # Fopt
	child.sendline("") # Max allowable error
	child.sendline("A") # Output ASCII/Binary

	## Do not remove. Blocks thread until ctrack has finished running
	output = []
	for i in range(9):
		child.readline()
		#print(child.readline())
	child.sendline("")

	return output

def velocityProcessing(sourcefile, destinationfile):
	child = pexpect.spawn("java WindowedAverage " + sourcefile + " " + destinationfile)
	for i in range(5):
		child.readline()

rawdirectory = "../RawData/"
finishedDirectory = "../Data/"
file = "q_hig_5"

print("Ctracking: " + file)
ctrack(rawdirectory,file, fopt=40)
print("Velocity processing: " + file)
velocityProcessing(rawdirectory+file, finishedDirectory+file)
print("Finished: " + file)
'''for file in getFileList(rawdirectory):
	print("Ctracking: " + file)
	ctrack(rawdirectory,file, fopt=40)
	print("Velocity processing: " + file)
	velocityProcessing(rawdirectory+file, finishedDirectory+file)
	print("Finished: " + file)
	print()'''
