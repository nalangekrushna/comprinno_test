n = 6
inputs = [
    [1,2,3,2,1],
    [2, 3, 4, 5, 4, 3, 2],
    [1, 2, 3, 4, 3],
    [1, 3, 5, 3, 1],
    [1, 2, 3, 4, 3, 2, 1],
    [1, 2, 3, 2]
]

def find_valid_land_strip(inputs) :
    results = []
    for lst in inputs :
        # if length of lst is even or land didn't start from 1 then didn't satisfy constraints.
        if lst[0] != 1 or len(lst) % 2 == 0 :
            results.append('no')
        else :
            middle = (len(lst) // 2)
            for i in range(len(lst)-1) :
                if i < middle :
                    # upto centre right value ie. next element should be greter than prev element.
                    if lst[i+1]-lst[i] != 1 :
                        results.append('no') 
                        break
                else :
                    # after centre left value ie. prev element should be greter than next element.
                    if lst[i]-lst[i+1] != 1 :
                        results.append('no')
                        break
            else :
                # if all constraints are satisfied then return yes.
                results.append('yes')
    return results

print(find_valid_land_strip(inputs))