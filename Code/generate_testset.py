#For one scanf line
import sys
import random
import os
import re


def random_int_generator():
	return random.randint(0, 1000)
	#return random.randint(-2**15 + 1, 2**15 - 1)
	
def random_long_generator():
	return random.randint(-2**31 + 1, 2**31 - 1)	

def random_longlong_generator():
	return random.randint(-2**63 + 1, 2**63 - 1)	

def random_unsigned_generator():
	return random.randint(0, 2**16 - 1)	
	
def random_unsignedlong_generator():
	return random.randint(0, 2**32 - 1)	
	
def random_unsignedlonglong_generator():
	return random.randint(0, 2**64 - 1)		
	
def random_unsignedshort_generator():
	return random.randint(0, 1000)
	
def random_float_generator():
	return random.uniform(-2**31 + 1, 2**31 - 1).format('0.6') #Get only 6 floating digits 	

def parse_line(new_line):
	test_vals = []
	for ele in new_line:
		if(ele == '%s'):
			test_vals.append(random_unsignedshort_generator())
		if(ele == '%d'):
			test_vals.append(random_int_generator())
		if(ele == '%ld' or ele == '%l'):
			test_vals.append(random_long_generator())
		if(ele == '%lld'):
			test_vals.append(random_longlong_generator())
		if(ele == '%u'):
			test_vals.append(random_unsigned_generator())
		if(ele == '%lu'):
			test_vals.append(random_unsignedlong_generator())
		if(ele == '%llu'):
			test_vals.append(random_unsignedlonglong_generator())							
		if(ele == '%f'):
			test_vals.append(random_float_generator())
		if(ele == '%lf'):
			test_vals.append(random_double_generator())
		if(ele == '%hu'):
			test_vals.append(random_unsignedshort_generator())	
	return test_vals		
	#print " ".join(map(str,test_vals))
			

def run(data_path):
	ASSERT_FAIL = "Assertion Failed"
	DATA_PATH =  data_path
	REF_PATH = DATA_PATH + "/reference.c"
	INPUT_TESTSET_FILE_PATH = DATA_PATH+"/input_automated.in"
	OUTPUT_TESTSET_FILE_PATH = DATA_PATH+"/output_automated.out"

	MAX_NUM_TESTS = 200

	format_strings = ['%d','%l','%ld','%lld','%u','%lu','%c','%s','%f','%lf', '%hu']



	test_set = []			

	#Create test-set from reference solution

	with open(REF_PATH,'r') as fin:
		lines = fin.readlines()
		for line in lines:
			if('scanf' in line):
				line = line.strip() #remove trailing whitespaces
				line = line.split('scanf(')[1].split(',')[0].strip('"').split()
				for num_tests in xrange(MAX_NUM_TESTS):
					test_set.append(parse_line(line))
				break

		
	#Get output for each input		

	outputs = []

	set_test = test_set[:]
	os.system("gcc -std=c11 -o a.out " + REF_PATH + " -lm")
	for test_case in test_set:
		val = " ".join(map(str,test_case))
		os.system("echo " + val + " > test.test")
		os.system("./a.out < test.test > result.result")
		#print test_case
		with open("result.result",'r') as fout:
			result = fout.readline()
			result = result.strip('\n').strip('\t').strip(' ')
			result = re.sub(' +', ' ',result)
			#print result
			if(result!=''):
				outputs.append(result) 	
			else:	
				outputs.append(ASSERT_FAIL)		#If file is empty probably assertion failed. Be careful if output is actually empty string, it still comes here.	
		os.system("rm -rf test.test result.result")	

	for i in xrange(len(test_set)):
		if(outputs[i]==ASSERT_FAIL):
			test_set[i] = ASSERT_FAIL

	#Store in input.in file
	with open(INPUT_TESTSET_FILE_PATH,'w') as fin:
		for test_case in test_set:
			if(test_case!=ASSERT_FAIL):
				fin.write("%s\n"%(" ".join(map(str,test_case))))			
		
	with open(OUTPUT_TESTSET_FILE_PATH,'w') as fin:
		for output in outputs:
			if(output!=ASSERT_FAIL):
				fin.write("%s\n"%output)			
