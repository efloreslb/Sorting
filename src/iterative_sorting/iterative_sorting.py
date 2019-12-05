# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        print(f'cur_index is {cur_index}')
        for x in range(cur_index + 1, len(arr) - 1):
            if arr[x] < arr[smallest_index]:   
                smallest_index = x
            else:
                pass
        
        print(f'smallest_index is {smallest_index} with number {arr[smallest_index]}')
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        # TO-DO: swap

    print(smallest_index)
    return arr

print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr