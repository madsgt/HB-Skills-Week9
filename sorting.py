#Sorting

def bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    pass

    while lst:
        for i in range(len(lst)-1): #go through all items but last 
            been_swap = False #check if we have done a swap
            for j in range(len(lst)-1 -i): #remove the ith item while looping again
                if lst[j] > lst[j+1]: #compare the jth item with the next item
                    lst[j], lst[j+1] = lst[j+1], lst[j] #swap if jth item is larger than next item
                    been_swap = True # we state the swap to have happened
            if not been_swap: #if already sorted and no swap reqd break out of the while loop
                break
                




def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    result_list = []

    while len(list1)>0 or len(list2)>0: # to check as long as list is not empty and has items
        if list1 == []: #if the list 1 is empty than pop and append the list 2 first 
            result_list.append(list2.pop(0))
        elif list2 == []: #if the list 2 is empty than pop and append the list 1 first 
            result_list.append(list1.pop(0))
        elif list1[0] > list2[0]: #if the first item of list 1 is greater than first item in list 2, pop and append the list 2 first item
            result_list.append(list2.pop(0))
        else: #else if the first item of list 1 is lesser than first item in list 2, pop and append the list 1 first item
            result_list.append(list1.pop(0))

    return result_list

    


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    thin input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    
    # part 1 -take all items and divide them in halves till there is only one item in the list
    # base case is when the list has only one item 
    if len(lst) < 2:
        return lst

    mid = int(len(lst)/2) #halve the list and index it there
    list1 = merge_sort(lst[:mid]) #create 2 lists ,divide the list in half and keep doing that on the way down
    list2 = merge_sort(lst[mid:])


    # part 2- merge the lists till we get one merged sorted list
    # on the way up keep sorting and merging the list

    result_list = []

    while len(list1)>0 or len(list2)>0: # to check as long as list is not empty and has items
        if list1 == []: # if the list 1 is empty than pop and append the list 2 first 
            result_list.append(list2.pop(0))
        elif list2 == []: # if the list 2 is empty than pop and append the list 1 first 
            result_list.append(list1.pop(0))
        elif list1[0] > list2[0]: # if the first item of list 1 is greater than first item in list 2, pop and append the list 2 first item
            result_list.append(list2.pop(0))
        else: # else if the first item of list 1 is lesser than first item in list 2, pop and append the list 1 first item
            result_list.append(list1.pop(0))

    return result_list



#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print