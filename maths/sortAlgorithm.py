
# Libraries to import
import time
from tabulate import tabulate
import itertools


class sort_algorithm:
    """A library with the following sorting algorithms
    
     * Bubble Sort = bubbleSort
     * Insertion Sort = insertionSort
     * Merge Sort   = mergeSort
     * Counting Sort = countingSort
     * Heap Sort = heapSort
     * Quick Sort = quickSort
     * Radix Sort = radixSort
     * Time test = test_run_time
    """

    # Instans of the class
    def __init__(self):
        pass

############################################################################################

    def bubbleSort(self, arr):
        """ 
        Bubble Sort. 
        Sorts an unordered list.
        Fast for a list below 1000 elements.

        Args:
            [list]: Integer and floats.
        
        Returns:
            [list]: Sorted list.
        """

        # https://www.youtube.com/watch?v=nmhjrI-aW5o&ab_channel=GeeksforGeeks
        
        # Gets the length og the array
        n = len(arr)
    
        # Traverse through all array elements
        for i in range(n):
    
            # Last i elements are already in place
            for j in range(0, n-i-1):
    
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    #print(arr) # print the list to see the operations 
                    #print(arr[j], "swapped place with", arr[j+1]) # prints which two numbers swap places

        return arr

############################################################################################
    
    
    def insertionSort(self, arr):
        """
        Insertion Sort.
        Sorts an unordered list.

        Args:
            [list]: Integer and floats.

        Returns:
            [list]: Sorted list.
        """
        # https://www.youtube.com/watch?v=OGzPmgsI-pQ&ab_channel=GeeksforGeeks

        # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):
    
            key = arr[i]
    
            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i-1
            while j >= 0 and key < arr[j] :
                    arr[j + 1] = arr[j]
                    j -= 1
            arr[j + 1] = key
    
        return arr

############################################################################################
   
    def __merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)

        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
        i = 0	 # Initial index of first subarray
        j = 0	 # Initial index of second subarray
        k = l	 # Initial index of merged subarray

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    # l is for left index and r is right index of the
    # sub-array of arr to be sorted

    
    def mergeSort(self, arr, l, r):
        """Merge Sort
           Divide and Conquer algorithm.
           Sorts an unordered list.

        Args:
            [array, start, end]
                array (List): Integers or floats.
                start (int): The first index number. (0)
                end (int): The last index number. (len(arr)-1)

        Returns:
            [list]: Sorted list.
        """

        if l < r:

            # Same as (l+r)//2, but avoids overflow for
            # large l and h
            m = l+(r-l)//2

            # Sort first and second halves
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m+1, r)
            self.__merge(arr, l, m, r)

        return arr
          
############################################################################################
    
    
    def countingSort(self, arr):
        """Counting Sort.
           Sorts an unordered list.

        Args:
            [list]: Integer.

        Returns:
            [list]: Sorted list.
        """

        # https://www.youtube.com/watch?v=7zuGmKfUt7s&ab_channel=GeeksforGeeks

        max_element = int(max(arr))
        min_element = int(min(arr))
        range_of_elements = max_element - min_element + 1
        # Create a count array to store count of individual
        # elements and initialize count array as 0
        count_arr = [0 for _ in range(range_of_elements)]
        output_arr = [0 for _ in range(len(arr))]
    
        # Store count of each character
        for i in range(0, len(arr)):
            count_arr[arr[i]-min_element] += 1
    
        # Change count_arr[i] so that count_arr[i] now contains actual
        # position of this element in output array
        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i-1]
    
        # Build the output character array
        for i in range(len(arr)-1, -1, -1):
            output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
            count_arr[arr[i] - min_element] -= 1
    
        # Copy the output array to arr, so that arr now
        # contains sorted characters
        for i in range(0, len(arr)):
            arr[i] = output_arr[i]
    
        return arr

############################################################################################

    def __heapify(self, arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2
    
        # See if left child of root exists and is
        # greater than root
        if l < n and arr[largest] < arr[l]:
            largest = l
    
        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r
    
        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
    
            # Heapify the root.
            self.__heapify(arr, n, largest)
    
    # The main function to sort an array of given size
    
    
    def heapSort(self, arr):
        """Heap Sort.
           Sorts an unordered list.

        Args:
            [list]: Integer and floats.

        Returns:
            [list]: Sorted list.
        """

        # https://www.youtube.com/watch?v=MtQL_ll5KhQ&ab_channel=GeeksforGeeks

        n = len(arr)
    
        # Build a maxheap.
        for i in range(n//2 - 1, -1, -1):
            self.__heapify(arr, n, i)
    
        # One by one extract elements
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            self.__heapify(arr, i, 0)
        
        return arr

############################################################################################

    def __partition(self, start, end, array):
        
        # Initializing pivot's index to start
        pivot_index = start 
        pivot = array[pivot_index]
        
        # This loop runs till start pointer crosses 
        # end pointer, and when it does we swap the
        # pivot with element on end pointer
        while start < end:
            
            # Increment the start pointer till it finds an 
            # element greater than  pivot 
            while start < len(array) and array[start] <= pivot:
                start += 1
                
            # Decrement the end pointer till it finds an 
            # element less than pivot
            while array[end] > pivot:
                end -= 1
            
            # If start and end have not crossed each other, 
            # swap the numbers on start and end
            if(start < end):
                array[start], array[end] = array[end], array[start]
        
        # Swap pivot element with element on end pointer.
        # This puts pivot on its correct sorted place.
        array[end], array[pivot_index] = array[pivot_index], array[end]
        
        # Returning end pointer to divide the array into 2
        return end
        
    # The main function that implements QuickSort 

    
    def quickSort(self, start, end, array):
        """Quick Sort.
           Sorts an unordered list.

        Args:
            [start, end, array]
                start (int): The first index number. ex:(0)
                end (int): The last index number. ex: (len(arr)-1) 
                array (List): Integers or floats.
            
        Returns:
            [list]: Sorted list.
        """

        # https://www.youtube.com/watch?v=PgBzjlCcFvc&ab_channel=GeeksforGeeks

        if (start < end):
            
            # p is partitioning index, array[p] 
            # is at right place
            p = self.__partition(start, end, array)
            
            # Sort elements before partition 
            # and after partition
            self.quickSort(start, p - 1, array)
            self.quickSort(p + 1, end, array)
        
        return array

############################################################################################

    # Python program for implementation of Radix Sort
    # A function to do counting sort of arr[] according to
    # the digit represented by exp.
    
    def __countingSort_radix(self, arr, exp1):
    
        n = len(arr)
    
        # The output array elements that will have sorted arr
        output = [0] * (n)
    
        # initialize count array as 0
        count = [0] * (10)
    
        # Store count of occurrences in count[]
        for i in range(0, n):
            index = arr[i] // exp1
            count[index % 10] += 1
    
        # Change count[i] so that count[i] now contains actual
        # position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]
    
        # Build the output array
        i = n - 1
        while i >= 0:
            index = arr[i] // exp1
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
    
        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]
    
    # Method to do Radix Sort


    def radixSort(self, arr):
        """Radix Sort.
           Sorts an unordered list.

        Args:
            [List]: Integer. 

        Returns:
            [List]: Sorted list.
        """

    # https://www.youtube.com/watch?v=nu4gDuFabIM&ab_channel=GeeksforGeeks

        # Find the maximum number to know number of digits
        max1 = max(arr)
    
        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        while max1 / exp > 0:
            self.__countingSort_radix(arr, exp)
            exp *= 10

        return arr
    
############################################################################################


    def test_run_time(self, arr):
        """Run each algorithm and time its run-time. 
        Prints the times of the algorithms ranked by the fastest. 

        Args:
            arr (list): integers or floats
        """
        array_length = len(arr)-1
        result_array = []
        time_array = []

        name_list = ['BubbleSort', 'InsertionSort', 'Mergesort', 'CountingSort','HeapSort', 'QuickSort', 'RadixSort']

        # List of sorting algorithms to call
        algorithm = [
        self.bubbleSort(arr),
        self.insertionSort(arr),
        self.mergeSort(arr, arr[0], array_length), 
        self.countingSort(arr),self.heapSort(arr),
        self.quickSort(arr[0], array_length, arr),
        self.radixSort(arr)
        ]

        # Iterate each sorting algorithm and time its execution
        for sort in algorithm:
            t_start = time.time()
            result_array.append(sort)
            t_end = time.time()
            time_array.append(t_end-t_start)
        
        # Verify all results are the same
        equal_results = False;
        if len(result_array) > 0 :
            equal_results = all(elem == result_array[0] for elem in result_array)
        
        # Prints result of the run-time test
        if equal_results:
            
            data = [
            [name_list[0],time_array[0],time_array[0]*60], 
            [name_list[1],time_array[1],time_array[1]*60], 
            [name_list[2],time_array[2],time_array[2]*60], 
            [name_list[3],time_array[3],time_array[3]*60], 
            [name_list[4], time_array[4],time_array[4]*60],
            [name_list[5], time_array[5],time_array[5]*60],
            [name_list[6], time_array[6],time_array[6]*60]
            ]
            data.sort(key=lambda x:x[1]) # sort array based on second element
            i = 1
            for elem in data:
                elem.insert(0, i)
                i += 1

            print(tabulate(data, headers=['No.','Algorithm','Time(sec)','Time(min)'])) 

        # Not all results are equal
        else:        
            print("[FAIL] Not all results are equal") # Error description

   

############################################################################################
