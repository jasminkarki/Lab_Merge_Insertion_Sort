from mergesort import merge_sort,merge
from insertionsort import insertion_sort
from time import time
import random
import matplotlib.pyplot as plt

time_arr=[]
size_arr=[]
#for i in range(0,1100,100): 			#For insertion sort
for i in range(10000,110000,10000):	#For merge sort
	size_arr.append(i)
	random_values = random.sample(range(i),i)
	value_length=len(random_values)
	start=time()
	# insertion_sort(random_values)
	merge_sort(random_values)
	end=time()
	time_arr.append(end-start)
	print(end-start)
	
#Plotting	
plt.plot(size_arr,time_arr)
plt.title("MERGE  SORT")				#For Merge Sort
# plt.title("INSERTION SORT")				#For Insertion Sort
plt.xlabel("Random Values")
plt.ylabel("Time taken (in seconds)")
plt.show()