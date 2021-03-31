def get_game_value(a,b,n) :
    # loop until n
    for i in range(n) :
        # for even no its alice turn
        if i%2==0 :
            a *=2
        # for odd no its bob turn
        else :
            b *=2
    return max(a,b)//min(a,b)

print(get_game_value(3,7,2))
    