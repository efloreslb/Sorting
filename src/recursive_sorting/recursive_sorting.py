# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
   elements = len( arrA ) + len( arrB )
   # merged_arr = [0] * elements
   merged_arr = []
   # TO-DO
   print(f'merged_arr: {merged_arr}')

   while len(arrA) > 0 and len(arrB) > 0:
      if arrA[0] > arrB[0]:
         merged_arr.append(arrB[0])
         arrB.remove(arrB[0])
      else: 
         merged_arr.append(arrA[0])
         arrA.remove(arrA[0])

   print(f'arrA: {arrA}')
   print(f'arrB: {arrB}')

   while len(arrA) > 0:
      merged_arr.append(arrA[0])
      arrA.remove(arrA[0])
   
   while len(arrB) > 0:
      merged_arr.append(arrB[0])
      arrB.remove(arrB[0])
   
   print(f'arrA: {arrA}')
   print(f'arrB: {arrB}')
    
   return merged_arr

print(merge([4,2,8], [3,1,9]))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
   if len(arr) <= 1:
      return arr

   half = (len(arr)/2)
   print(int(half))

   arr1 = arr[:int(half)]
   print(arr1)

   arr2 = arr[int(half):]
   print(arr2)

   return merge(merge_sort(arr1), merge_sort(arr2))

   # merge_sort()

   # return arr

print(f'merge_sort: {merge_sort([14, 20, 1, 5, 0, 4])}')
# print(f'merge_sort: {merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])}')

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
   # TO-DO

   return arr

def merge_sort_in_place(arr, l, r): 
   # TO-DO

   return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
