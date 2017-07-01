def dec_to_bin(num):
    bin_l = []
    remainder = num
    while remainder > 0:
        if remainder % 2 == 0:
            next = "0"
        else:
            next = "1"
        bin_l.append(next)
        remainder = remainder / 2

    reversed_bin = reversed(bin_l)
    final = ''.join(reversed_bin)

    return final

def bin_to_dec(num_str):
    num_l = []
    for item in num_str:
        num_l.append(item)
    reverse_str = reversed(num_l)
    num = ''.join(reverse_str)

    num_sum = 0
    for i in range(len(num)):
        if num[i] == "1":
            num_sum += 2**i
        # if num[i] == "0":
            #num_sum += (2**i) * 0
        # else:
            # num_sum += (2**i) * 1
    return num_sum

