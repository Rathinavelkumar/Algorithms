def BinarySearch(arr, search):
    start, end, index = 0, len(arr)-1, -1
    while start<=end and index==-1:
        mid = (start+end)//2
        if arr[mid]==search:
            index=mid
        elif search<arr[mid]:
            end=mid-1
        else:
            start=mid+1
    return index

input_array = [1,2,3,4,5,6,7,8,9,10]
search_number = 0
result = BinarySearch(input_array, search_number)
print(result)