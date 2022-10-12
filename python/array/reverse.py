def reverse(arr:int):
    i = 0
    j = len(arr) - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i, j = i+1, j-1
    print(arr)
   


reverse([1,2,4,5])

---------------------

def reverse(arr:list[int], l, r):
    if l==r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    
    reverse(arr, l+1, r-1)
    print(arr)
    

reverse([1,2,3,4,5], 0, 4)


