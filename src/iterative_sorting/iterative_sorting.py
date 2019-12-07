# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # print(f'cur_index is {cur_index}')
        for x in range(cur_index, len(arr)):
            if arr[x] < arr[smallest_index]:   
                smallest_index = x
                # print(f'smallest_index - {smallest_index} number {arr[smallest_index]}')
        
        # print(f'smallest_index is {smallest_index} with number {arr[smallest_index]}')
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        # TO-DO: swap

    # print(smallest_index)
    return arr

print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
print(selection_sort([0, 1, 2, 3, 4, 5]))
print(selection_sort([]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # sorted = False

    # while not sorted:

    #     swap = True

    #     for i in range(0, len(arr) - 1):
    #         cur_index = i
            
    #         if swap == True:
    #             if arr[cur_index] > arr[cur_index + 1]:
    #                 arr[cur_index], arr[cur_index + 1] = arr[cur_index + 1], arr[cur_index]
    #             else:
    #                 swap = False
    #         else:
    #             sorted = True

    for i in range(0, len(arr) - 1):

        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(f'bubble {bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])}')


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr