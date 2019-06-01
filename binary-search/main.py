import math


# declare binary search function
def binary_search(arr_num, search):
    lo_index = 0
    hi_index = len(arr_num) - 1

    while lo_index <= hi_index:
        print("searching in: " + str(arr_num[lo_index:hi_index + 1]))
        middle_index = math.floor((lo_index + hi_index) / 2)

        middle_num = arr_num[middle_index]

        if search == middle_num:  # if found, nice
            print("FOUND!: " + str(arr_num[middle_index]))
            break
        elif search < middle_num:
            hi_index = middle_index - 1  # minus 1 so we will not include the middle number that has been validated
        elif search > middle_num:
            lo_index = middle_index + 1  # add 1 so we will not include the middle number that has been validated
        else:
            print("NUMBER NOT FOUND :(")
            break


# test binary searching!
sorted_list = list(range(1000))
search_for = 69

print(binary_search(sorted_list, search_for))
