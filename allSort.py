import random

#######################################################Quick Sort #########################################################################
def quickSort(arr) : 
    #  print("Quick sort")

    if len(arr) <= 1 : 
        return arr

    pivot = arr[len(arr)/2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quickSort(left) + middle + quickSort(right)


#######################################################Merge Sort #########################################################################
def merge(a,b) : 
    c = []

    while len(a) != 0 and len(b) !=0 : 
        if a[0] < b[0] : 
            c.append(a[0])
            a.remove(a[0])
        else : 
            c.append(b[0])
            b.remove(b[0])

    if len(a) == 0 : 
        c += b
    else : 
        c += a

    return c


def mergeSort(arr) : 
    print("Merge sort")

    if len(arr) == 1 or len(arr) == 0 : 
        return arr
    else : 
        middle = len(arr)/2
        a = mergeSort(arr[:middle])
        b = mergeSort(arr[middle:])
        return merge(a,b)

#######################################################Insertion Sort #########################################################################
def swap(arr, a, b) : 
    arr[a],arr[b] = arr[b],arr[a]

def insertionSort(arr) : 
    print("Insertion Sort")

    change = 0; index = 0; posn=0; currVal = 0

    for index in range(0,len(arr)-1) : 
        if arr[index] > arr[index+1] : 
            currVal = arr[index + 1]
            posn = index+1

        while posn > 0 and currVal < arr[posn-1] : 
            swap(arr, posn-1, posn)
            posn-=1

    return arr

#######################################################Selection Sort #########################################################################
def findMin(arr) : 

    iMin = arr[0]
    for x in arr : 
        if x < iMin : 
            iMin = x

    return iMin

def findMinIndex(arr) : 

    iMin = 0
    for index in range (0,len(arr)) : 
        if arr[index] < arr[iMin] : 
            iMin = index

    return index


def selectionSort(arr) : 
    print("Selection Sort")

    for i in range(0,len(arr)) : 
        for j in range(i+1, len(arr)) : 
            if arr[i] > arr[j] : 
                swap(arr,i,j)

    return arr


#######################################################Heap Sort #########################################################################
def heapify(arr, n, i) : 
    largest = i
    l = 2*i+ 1  # left child
    r = 2*i+ 2 # right child

#Check if left child exists and is greater than the root
    if l < n and arr[i] < arr[l] : 
        largest = l

#Check if right child exists and is greater than the root
    if r < n and arr[largest] < arr[r] : 
        largest = r

#Swap the root if needed and heapify the root again
    if largest != i : 
        swap(arr, largest,i)
        heapify(arr, n, largest)

#    return arr


def heapSort(arr) : 
    arrSize = len(arr)

    # Build a maxheap.
    for i in range(arrSize, -1, -1):
        heapify(arr, arrSize, i)

    # One by one extract elements
    for i in range(arrSize-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)

    return arr


#######################################################Selection Sort #########################################################################
def bubbleSort(arr) : 

    for j in range(0, len(arr)) : 
        for i in range(0, len(arr)-1) : 
            if arr[i] > arr[i+1] : 
                swap(arr,i,i+1)

    return arr


#######################################################MAIN#########################################################################
def main() : 

    print("********This is a program which implements various sorts***********")
    numSorts = 6

    print(" *******The sorting algorithms are numbered as shown below*************")
    print("\n")
    print("1 : Quick Sort")
    print("2 : Merge Sort")
    print("3 : Insertion Sort")
    print("4 : Selection Sort")
    print("5 : Heap Sort")
    print("6 : Bubble Sort")

    sortNum = int(raw_input("enter the corresponding number of the sort that you want to try : "))

    while sortNum > numSorts : 
        print("Wrong Input") 
        sortNum = int(raw_input("enter the corresponding number of the sort that you want to try : "))

    numElements = 10 
    arr = [49,100,32,62,72,17,65,69,29,73]

#    arr = []
#    for x in range (0, numElements) : 
#        arr.append( int(random.randint(0,100)))

    print("\n")
    print(" Original array ")
    print(arr)
    print("\n")

    #QUICK SORT ****************************************
    if sortNum == 1 : 
        arr = quickSort(arr)
        print ("Quick Sorted array ")
        print(arr)
        print("\n")


    #Merge Sort ****************************************
    if sortNum == 2 : 
        arr = mergeSort(arr)
        print ("Merge Sorted array ")
        print(arr)
        print("\n")

    #Insertion Sort ****************************************
    if sortNum == 3 : 
        arr = insertionSort(arr)
        print ("Insert Sorted array ")
        print(arr)
        print("\n")

    #Selection Sort ****************************************
    if sortNum == 4 : 
        arr = selectionSort(arr)
        print ("Selection Sorted array ")
        print(arr)
        print("\n")

    #Heap Sort ****************************************
    if sortNum == 5 : 
        arr = heapSort(arr)
        print ("Heap Sorted array ")
        print(arr)
        print("\n")

    #Bubble Sort ****************************************
    if sortNum == 6 : 
        arr = bubbleSort(arr)
        print ("Bubble Sorted array ")
        print(arr)
        print("\n")



if __name__ == '__main__' : 
    main()
