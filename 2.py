input_1 = [(1,2,3),(2,3,4),(2,3,5)] # 
input_2 = [(1,2,3),(2,3,4),(2,3,4)]
input_3 = [(5,6,5),(1,2,3),(2,3,4)]
input_4 = [(1,3,4),(1,2,3),(3,4,5)]
inputs = [input_1,input_2,input_3,input_4]

def sort_input(inputs) :
    sorted_input = []
    for inp in inputs :
        # sort lists according to their sum.
        sorted_input.append(sorted(inp, key = lambda x:x[0] + x[1]+ x[2])) 
    return sorted_input

def check_better_team(inputs) :
    sorted_input = sort_input(inputs)

    results = []
    for inp in sorted_input :             
        # inp = [(1,3,4),(1,2,3),(3,4,5)]
        for i in range(len(inp)-1) :
            # check if all elements are less or equal to elements in second tuple.
            if inp[i][0] <= inp[i+1][0] and inp[i][1] <= inp[i+1][1] and inp[i][2] <= inp[i+1][2] :
                # check difference between sum of all elements of second and first tuple is atleast one.
                if ((inp[i+1][0]-inp[i][0]) + (inp[i+1][1]-inp[i][1]) + (inp[i+1][2]-inp[i][2])) < 1 :
                    results.append('no')
                    break

            else :
                # if any element is greater than element is second tuple append no.
                results.append('no')
                break
        else :
            # loop ended by exhaustion. so all tuples in given last are following all the given conditions.
            results.append('yes')
    return results

print(check_better_team(inputs))