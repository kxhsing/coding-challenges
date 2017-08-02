def find_second_max(lst):
    """Given list of integers, find the second max int"""

    if len(lst) > 1:
        if lst[0] > lst[1]:
            largest = lst[0]
            second_lrg = lst[1]
        else:
            largest = lst[1]
            second_lrg = lst[0]

        for num in lst[2:]:
            if num > largest:
                second_lrg = largest
                largest = num
            elif num > second_lrg:
                second_lrg = num

        return second_lrg

    elif len(lst) == 1 :
        return lst[0]

    else:
        return None