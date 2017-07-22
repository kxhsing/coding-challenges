def firstDuplicate(a):

    a_set = set(a)
    if len(a_set) == len(a):
        return -1
    
    num_dic = {}
    for i, num in enumerate(a):
        if num in num_dic:
            return num
        else:
            num_dic[num] = [i]
    
