
def get_rectangle_area(sticks) :
    stick_count = {}
    for i in sticks :
        if i in stick_count :
            stick_count[i] += 1
        else :
            stick_count[i] = 1
    # filter only sticks having atleast two sticks of same length.
    stick_count = { k:v for k,v in stick_count.items() if v > 1 }
    # if all sticks are of same length and are atmax 3 so can't create rectangle.
    if len(stick_count) == 1 and list(stick_count.values())[0] <= 3 :
        return -1
    # if all sticks are of same length and are atleast 4 then special case of rectange square will form.
    elif len(stick_count) == 1 and list(stick_count.values())[0] > 3 :
        return list(stick_count.keys())[0]**2
    # if there are atleast sticks of two lenghts
    elif len(stick_count) > 1 :
        # sort them by highest to lowest using their count.
        two_elements = sorted(stick_count.keys(),reverse=True)[:2]
        # If atleast 4 elements are present then use that element only.
        if stick_count[two_elements[0]] > 3 :
            return two_elements[0]**2
        else :
            # take highest and second highest element.
            return two_elements[0]*two_elements[1]

print(get_rectangle_area([4,4,3,3,5,5,2,2,5,5]))
