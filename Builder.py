import re
import os
import sys
import datetime

OUTPUT = "output_" + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".txt"

print("**********************************************************")
print("[INFO]: Build process started")
print("**********************************************************")

cwd = os.getcwd()
repoPath = sys.argv[1]
print("[INFO]: The build process will concatenate the files BuildComponent_1, BuildComponent_2 and BuildComponent_3 into output file under bin")
print("[INFO]:Checking the repo path")
os.chdir(repoPath)

inputfile1 = open('BuildComponent_1.txt')
inputfile2 = open('BuildComponent_2.txt')
inputfile3 = open('BuildComponent_3.txt')
if not os.path.exists('bin'):
	os.mkdir('bin')
outputfile = open('bin' + '\\' + OUTPUT, 'w+')

print("[INFO] : Processing data from file BuildComponent_1.txt")
for line in inputfile1:    
    outputfile.write(line)

print("[INFO] : Processing data from file BuildComponent_2.txt")
for line in inputfile2:    
    outputfile.write(line)

print("[INFO] : Processing data from file BuildComponent_3.txt")
print("[INFO] : Preparing the file " + OUTPUT)
for line in inputfile3:
    outputfile.write(line)

	
inputfile1.close
inputfile2.close
inputfile3.close
outputfile.close

os.chdir(cwd)

print("**********************************************************")
print("[INFO]: build.bat completed successfully")
print("**********************************************************")