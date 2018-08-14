import sys
import glob
import os
import subprocess32
import time
import matplotlib.pyplot as plt
import re

def run(data_path, FLAGS_GEN_TESTSET):
	DATA_PATH = data_path
	CORRECT_SOL_PATH = DATA_PATH + "/Correct"
	INCORRECT_SOL_PATH = DATA_PATH + "/Incorrect"
	
	if(FLAGS_GEN_TESTSET): 
		INPUT_TESTSET_FILE_PATH = DATA_PATH+"/input_automated.in"
		OUTPUT_TESTSET_FILE_PATH = DATA_PATH+"/output_automated.out"	
	else:
		INPUT_TESTSET_FILE_PATH = DATA_PATH+"/input.in"
		OUTPUT_TESTSET_FILE_PATH = DATA_PATH+"/output.out"

	test_set = []
	outputs = []

	os.system("rm -rf " + CORRECT_SOL_PATH);
	os.system("rm -rf " + INCORRECT_SOL_PATH);

	os.system("mkdir " + CORRECT_SOL_PATH);
	os.system("mkdir " + INCORRECT_SOL_PATH);

	with open(INPUT_TESTSET_FILE_PATH,'r') as fin:
		lines = fin.readlines()
		for line in lines:
			test_set.append(line[:-1])

	with open(OUTPUT_TESTSET_FILE_PATH,'r') as fin:
		lines = fin.readlines()
		for line in lines:
			outputs.append(line[:-1])
		
	solutions = glob.glob(DATA_PATH+"/Solutions/*.c")

	#Remove files which won't compile
	temp = []
	for sol in solutions:
		os.system("gcc -static -fno-optimize-sibling-calls -fno-strict-aliasing -fno-asm -s -O2 -o a.out " + sol + " -w -lm")
		if os.path.isfile("a.out"):
			temp.append(sol)
			os.system("rm a.out")

	solutions = temp
	#print solutions
	print "Execution Starts"

	tot_runtimes = []
	grade_incorrect = {}		
	for sol in solutions:
		code_answer_set = []
		run_time = []
		grade = 0
		os.system("gcc -static -fno-optimize-sibling-calls -fno-strict-aliasing -fno-asm -s -O2 -o test.out " + sol + " -w -lm")
		for test_case in test_set:
			os.system("echo " + test_case + " > test.test")
			cmd = ["bash","-c","./test.out < test.test > result.result"]
			start = time.time()
			try:
				subprocess32.call(cmd, timeout = 3)
			except subprocess32.TimeoutExpired:
				code_answer_set.append("Timeout")
				run_time.append("Timeout")
				continue
			end = time.time()
			exec_time = end - start		
			with open("result.result",'r') as fout:
				result = fout.readline()
				result = result.strip('\n').strip('\t').strip(' ')
				result = re.sub(' +', ' ',result)
				code_answer_set.append(result)
			os.system("rm -rf test.test result.result")
			run_time.append(exec_time)
		total_runtime = 0		
		for i in xrange(len(outputs)):
			if(outputs[i]==code_answer_set[i]):
				grade+=1
				#print i
				total_runtime+=run_time[i]
			else:
				if(code_answer_set[i]!="Timeout" and "Incorrect" not in sol):
					print outputs[i], code_answer_set[i]	
		tot_runtimes.append(total_runtime)			
		
		print "Avg. Grade and Runtime of %s is %f and %f"%(sol.split('/')[-1], grade/float(len(outputs)), total_runtime/float(len(outputs)))
		os.system("rm -rf test.out")
		if(grade/float(len(outputs)) == 1):
			os.system("cp " + sol + " " + CORRECT_SOL_PATH);
		else:
			os.system("cp " + sol + " " + INCORRECT_SOL_PATH);
			grade_incorrect[sol.split('/')[-1]] = 	grade/float(len(outputs)) 
	return tot_runtimes, grade_incorrect		
	#plt.plot(tot_runtimes, tot_runtimes,  'ro')
	#plt.show()
	
