# merge sort
from random import randint

def merge(ls, l, m, r):
    tmp = []
    i = l
    j = m

    while i < m and j < r:
        if ls[i] < ls[j]:
            tmp.append(ls[i])
            i+=1
        else:
            tmp.append(ls[j])
            j+=1

    while i < m:
        tmp.append(ls[i])
        i+=1

    while j < r:
        tmp.append(ls[j])
        j+=1

    ls[l:r] = tmp[:]

def recursive_mergesort(ls,l,r):
    if l < r-1:
        m = (l + r)/2
        recursive_mergesort(ls,m,r)
        recursive_mergesort(ls,l,m)
        merge(ls,l,m,r)

def iterative_mergesort(ls):
    partition_size = 1
    while(partition_size < len(ls)):
        i = 0
        while ( i + partition_size < len(ls)-1):
            r = min(len(ls),i+2*partition_size)
            m = i + partition_size
            merge(ls,i,m,r)
            i += 2*partition_size
        partition_size = 2*partition_size

if __name__ == '__main__':
    arr = [randint(0,100) for i in range(0,100)]
    n = len(arr)
    print ("Given array is")
    for i in range(n):
        print ("{}".format(arr[i])),

    recursive_mergesort(arr,0,n)
    print ("\n\nRecursively sorted array is")
    for i in range(n):
        print ("{}".format(arr[i])),

    arr = [randint(0,100) for i in range(0,100)]
    n = len(arr)
    print ("\n\nGiven array is")
    for i in range(n):
        print ("{}".format(arr[i])),

    iterative_mergesort(arr)
    print ("\n\nIteratively sorted array is")
    for i in range(n):
        print ("{}".format(arr[i])),
