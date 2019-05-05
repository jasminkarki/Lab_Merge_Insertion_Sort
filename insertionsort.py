def insertion_sort(arr):
	for j in range (1,len(arr)):
		key=arr[j];
		#Insert A[j] into sorted sequence
		i=j-1
		while i>=0 and arr[i]>key:
			arr[i+1]=arr[i]
			i-=1
		arr[i+1]=key


