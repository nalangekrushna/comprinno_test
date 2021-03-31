inputs = [
    ['cookie', 'milk', 'milk', 'cookie', 'milk', 'cookie', 'milk',],
    ['cookie', 'cookie', 'milk', 'milk', 'milk'],
    ['milk','milk'],
    ['cookie']
]

def check_parents_instructions_violated(inputs) :
    results = []
    for lst in inputs :
        # if no cookie eaten means never need to check for milk after cookie.
        if 'cookie' not in lst :
            results.append('YES')
        else :
            for i in range(len(lst)) :
                # if cookie is eaten at last then condition violated.
                if lst[i] == 'cookie' and i == len(lst)-1 :
                    results.append('NO')
                    break
                # also can't eat cookie after cookie.
                elif lst[i] == 'cookie' and lst[i+1] == 'cookie' :
                    results.append('NO')
                    break
            else :
                # no conditon violted so adding YES.
                results.append('YES')
    return results

print(check_parents_instructions_violated(inputs))