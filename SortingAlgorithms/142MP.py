# sources:
# https://www.pythoncentral.io/selection-sort-implementation-guide/
# https://www.pythoncentral.io/bubble-sort-implementation-guide/
# https://www.pythoncentral.io/insertion-sort-implementation-guide/
# https://www.pythoncentral.io/merge-sort-implementation-guide/
# https://www.pythoncentral.io/quick-sort-implementation-guide/
# http://www.growingwiththeweb.com/2015/06/bucket-sort.html

# http://www.geeksforgeeks.org/radix-sort/
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-7.php
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheShellSort.html
# https://gist.github.com/siim-/2561003

# ---------------- O(n^2) algorithms (selection, bubble, insertion) STARTS HERE ---------------- #
import math


def selection_sort(_list):
    for i in range(len(_list)):

        # Find the minimum element in remaining
        min_element = i

        for j in range(i + 1, len(_list)):
            if _list[min_element] > _list[j]:
                min_element = j

        # Swap the found minimum element with min_element
        temp = _list[i]
        _list[i] = _list[min_element]
        _list[min_element] = temp

    return _list


def bubble_sort(_list):
    # Setting the range for comparison (first round: n, second round: n-1  and so on)
    for i in range(len(_list) - 1, 0, -1):

        # Comparing within set range
        for j in range(i):

            # Comparing element with its right side neighbor
            if _list[j] > _list[j + 1]:
                # swapping
                temp = _list[j]
                _list[j] = _list[j + 1]
                _list[j + 1] = temp

    return _list


def insertion_sort(_list):
    for i in range(1, len(_list)):

        # element to be compared
        current = _list[i]

        # comparing the current element with the sorted portion and swapping
        while i > 0 and _list[i - 1] > current:
            _list[i] = _list[i - 1]
            i = i - 1
            _list[i] = current

        # print(_list)

    return _list


# ---------------- O(n^2) algorithms (selection, bubble, insertion) STOPS HERE ---------------- #

# ---------------- Bucket sort (using insertion sort as subroutine) STARTS HERE ---------------- #

DEFAULT_BUCKET_SIZE = 1000


def sort(array, bucket_size=DEFAULT_BUCKET_SIZE):
    if len(array) == 0:
        return array

    # Determine minimum and maximum values
    min_value = array[0]
    max_value = array[0]
    for i in range(1, len(array)):
        if array[i] < min_value:
            min_value = array[i]
        elif array[i] > max_value:
            max_value = array[i]

    # Initialize buckets
    bucket_count = math.floor((max_value - min_value) / bucket_size) + 1
    buckets = []
    for i in range(0, bucket_count):
        buckets.append([])

    # Distribute input array values into buckets
    for i in range(0, len(array)):
        buckets[math.floor((array[i] - min_value) / bucket_size)].append(array[i])

    # Sort buckets and place back into input array
    array = []
    for i in range(0, len(buckets)):
        insertion_sort.sort(buckets[i])
        for j in range(0, len(buckets[i])):
            array.append(buckets[i][j])

    return array

# ---------------- Bucket sort (using insertion sort as subroutine) STOPS HERE ---------------- #

# ---------------- Merge sort vs Quick sort STARTS HERE ---------------- #


def merge_sort(_list):
    print("Splitting ", _list)

    if len(_list) > 1:
        mid = len(_list) // 2
        left_half = _list[:mid]
        right_half = _list[mid:]

        # recursion
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                _list[k] = left_half[i]
                i = i + 1
            else:
                _list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            _list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            _list[k] = right_half[j]
            j = j + 1
            k = k + 1

    print("Merging ", _list)


def quick_sort(_list):
    quick_sort_helper(_list, 0, len(_list) - 1)


def quick_sort_helper(_list, first, last):
    if first < last:
        split_point = partition(_list, first, last)
        quick_sort_helper(_list, first, split_point - 1)
        quick_sort_helper(_list, split_point + 1, last)


def partition(_list, first, last):
    pivot_value = _list[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and _list[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while _list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            temp = _list[left_mark]
            _list[left_mark] = _list[right_mark]
            _list[right_mark] = temp

    temp = _list[first]
    _list[first] = _list[right_mark]
    _list[right_mark] = temp

    return right_mark


# ---------------- Merge sort vs Quick sort STOPS HERE ---------------- #


# int main alike starts here


print("Selection sort: ", selection_sort([5, 2, 1, 9, 0, 4, 6]))
print("Bubble sort: ", bubble_sort([5, 1, 2, 3, 9, 8, 0]))
print("Insertion sort: ", insertion_sort([5, 2, 1, 9, 0, 4, 6]))

print("\n")
_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(_list)
print(_list)

print("\n")
_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(_list)
print("Quick sort: ", _list)
