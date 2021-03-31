inputs = [
    [0, 1],
    [1, 2],
    [5, 6]
]

def find_beautiful_pairs(inputs) :
    results = []
    for lst in inputs :
        # call pair function for every list
        results.append(pair(lst))
    return results

def pair(inputs) :
    # go through list twice to multiply with itself.
    for i, first in enumerate(inputs) :
        for j, second in enumerate(inputs) :
            # don't multiply same element from same positon
            if i == j :
                continue
            else :
                # check if multiplication is in input list.
                if first*second not in inputs :
                    return 'no'
    else :
        # satisfied all conditions so returning yes.
        return 'yes'

print(*find_beautiful_pairs(inputs),sep='\n')