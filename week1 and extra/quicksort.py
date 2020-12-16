arr = [10,16,8,12,15,6,3,9,5]

def partition(l, h):
    pivot = arr[l]
    i,j = l+1,h
    while True:
        while arr[i]<=pivot:
            i+=1
        while arr[j]>pivot:
            j-=1
        if i>=j:
            break
        arr[i],arr[j] = arr[j],arr[i]

    arr[l],arr[j] = arr[j],arr[l]
    return j

def quicksort(l,h):
    if l<h:
        j=partition(l,h)
        quicksort(l,j)
        quicksort(j+1,h)

print(arr)
quicksort(0,len(arr)-1)
print(arr)