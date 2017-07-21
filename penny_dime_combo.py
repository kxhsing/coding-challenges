def find_combo_values(nums):
    import itertools
        return {sum(combo) for combo in itertools.combinations([10,1]*nums, nums)}

def add_coins(num, coin1_val, coin2_val):
    results = set()
    # coin1_val = 10 #dime
    # coin2_val = 1 #penny
    for coin1 in range(num+1):
        coin2 = num - coin1 
        total = coin1*coin1_val + coin2*coin2_val
        results.add(total)
    return results