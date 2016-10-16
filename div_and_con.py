#! /bin/python

import random, pdb, sys, math

def Algo(array):
	return divAndConAlgo(array)

def divAndConAlgo(array):		# main function
	sumMax = 0
	mid = 0
	
	if len(array) == 2:# base case #1, 2 array element
		return max(array[0], array[1])
	elif len(array) == 1:# base case #2, 1 array element
		return array[0]
		
	else:
		mid = int(math.floor(len(array) / 2))		# // is floor division?

		sum_left = divAndConAlgo(array[0:mid])
		if mid+1 == len(array)-1:
			sum_right = array[mid+1]
		else:
			sum_right = divAndConAlgo(array[mid+1:len(array)-1])
		max_crossing_sum = sum_left_right(array)
		

		return max(sum_left, sum_right, max_crossing_sum)

#Find the maximum possible sum in arr[] auch that arr[m] is part of it
def sum_left_right(array):
	min_int = -(sys.maxint-1)
	mid = int(math.floor(len(array) / 2))		# // is floor division?

	#Include elements on left of mid.
	sum = 0;
	left_sum = min_int;
	for i in range(0, mid):
		sum = sum + array[i]
		if sum > left_sum:
			left_sum = sum

	#Include elements on right of mid
	sum = 0;
	right_sum = min_int;
	for i in range(mid+1, len(array)-1):
		sum = sum + array[i];
		if sum > right_sum:
			right_sum = sum;

	#Return sum of elements on left and right of mid
	return left_sum + right_sum;

if __name__ == "__main__":

  arr = [int(1000*random.random()) for i in xrange(10)]
  result = divAndConAlgo(arr)
  pdb.set_trace()
