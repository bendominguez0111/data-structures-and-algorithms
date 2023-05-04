"""
Given an unsorted array, do a bubble sort O(n^2) to sort the array.
"""



def bubble_sort(arr):

    n = len(arr)

    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

if __name__ == '__main__':
    arr = [5, 2, 3, 10, 8, 7, 16, 2, 1, 1, 4]
    sorted_arr = bubble_sort(arr)
    print(sorted_arr) #[1, 1, 2, 2, 3, 4, 5, 7, 8, 10, 16]
