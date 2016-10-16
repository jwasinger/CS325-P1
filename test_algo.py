#! /usr/bin/python

import os, sys
import div_and_con

def extract_list(list_str):
#remove uneccessary characters from list string and split (delimit by commas) into a list
	return map(lambda x: int(x), ''.join(c for c in list_str if c not in '[]\r\n ').split(','))

def load_problems(file_name):
	with open(file_name) as f:
		content = f.readlines()
		return map(lambda x: extract_list(x), content)

def load_results(file_name):
	with open(file_name) as f:
		content = f.readlines()
		return map(lambda x: int(x), content)

if __name__ == '__main__':
	problems = load_problems(os.path.join(os.getcwd(), 'MSS_TestProblems-1.txt'))
	results = load_results(os.path.join(os.getcwd(), 'MSS_TestResults.txt'))
	if len(problems) != len(results):
		print("error, Mismatch between number of problems/results in given test files")
		sys.exit(-1)
	for i in range(0, len(problems) - 1):
		result = div_and_con.Algo(problems[i])
		if result != results[i]:
			print("algorithm incorrect: ")
			print(problems[i])
			print(results[i])
			print(result)
			sys.exit(-1)

	import pdb; pdb.set_trace()
