def linear_search(arr, search):
    for index, each in enumerate(arr):
        if each==search:
            return index
    return -1

input_array = [1, 2, 3, 4, 5, 2, 8, 7]
search_number = 8
result = linear_search(input_array, search_number)
print(result)