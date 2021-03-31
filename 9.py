def rec_func(lst,cost) :
    # if list contains last element then return it as value.
    if len(lst) == 1 :
        return lst[0],cost
    # find min, max from list, add min to cost and remove max from list.
    else :
        cost += min(lst[0],lst[1])
        lst.remove(max(lst[0],lst[1]))
        return lst,cost

def get_min_cost_of_operation(lst) :
    cost = 0
    # until return type of lst is list call function
    while isinstance(lst,list) :
        lst,cost = rec_func(lst,cost)
    return cost
    

print(get_min_cost_of_operation([4,2,5]))
