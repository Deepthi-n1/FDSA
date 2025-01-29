A=[10,89,9,56,4,80,8]
 largest=arr[0]
 smallest=arr[0]

    for num in arr:
    	    if num > largest:
	    	    largest = num
	         if num < smallest:
		         smallest = num

         return largest,smallest