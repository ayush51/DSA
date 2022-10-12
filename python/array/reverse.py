def reverse(arr:int):
    i = 0
    j = len(arr) - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i, j = i+1, j-1
    print(arr)
   


reverse([1,2,4,5])
