import os
import sys
import glob
import subprocess32
test_set = []
actual_answer_set = []

folder = sys.argv[1]
DATA_PATH = "/home/perseus/Academics/Sem-9/Thesis/Data/CodeForces/"
incorr_files = glob.glob(DATA_PATH+folder+"/Incorrect/*.c")

with open(DATA_PATH+folder+"/input.in",'r') as fin:
	lines = fin.readlines()
	for line in lines:
		test_set.append(line[:-1])

with open(DATA_PATH+folder+"/output.out",'r') as fin:
	lines = fin.readlines()
	for line in lines:
		actual_answer_set.append(line[:-1])
		
for file1 in incorr_files:
	print file1.split("/")[-1]
	code_answer_set = []
	os.system("gcc -w -std=c11 -o a.out " + file1 + " -lm")
	for test_case in test_set:
		os.system("echo " + test_case + " > test.test")
		cmd = ["bash","-c","./a.out < test.test > result.result"]
		try:
			subprocess32.call(cmd, timeout = 1)
		except subprocess32.TimeoutExpired:
			code_answer_set.append("Timeout")
			continue	
		with open("result.result",'r') as fout:
			result = fout.readline()
			code_answer_set.append(result.split("\n")[0])
	os.system("rm -rf test.test result.result")

	count=0

	for i in xrange(len(test_set)):
		if(code_answer_set[i]==actual_answer_set[i]):
			count+=1
	acc = float(count*100)/len(test_set)
	print "Accuracy for %s: %f"%(file1.split('/')[-1],acc)
	with open(DATA_PATH+folder+"/marks","a") as fout:
		val = 0
		if(acc>80):
			val = 2
		elif(acc>60 and acc<=80):
			val = 1.5
		elif(acc>45 and acc<=60):
			val = 1			
		fout.write("%s %f\n"%(file1.split('/')[-1],val))
