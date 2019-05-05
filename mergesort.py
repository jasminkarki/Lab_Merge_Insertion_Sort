def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[0:mid]
        right=arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(arr,left,right)
    
       
def merge(arr,left,right):
	i=j=k=0
	n1=len(left)
	n2=len(right)
	while(i<n1 and j<n2):
		if left[i]<=right[j]:
			arr[k]=left[i]
			i=i+1
		else:
			arr[k]=right[j]
			j=j+1
		k=k+1
	'''
		L= 1,3	|	n1=2
		R= 2,4	|	n2=2
		i=0 and j=0 1vs2->Push 1, i=1
		i=1 and j=0 3vs2->Push 2, j=1
		i=1 and j=1 3vs4->Push 3, i=2
		
		Here 1,2 and 3 got pushed but 4 left.
	'''
	#So, for remaining elements.
	while (i<n1):
		arr[k]=left[i]
		k=k+1
		i+=1

	while (j<n2):
		arr[k]=right[j]
		k=k+1
		j+=1