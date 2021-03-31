c=1
d=1
l=9

def validate_leg_count(c,d,l) :
    # as dogs and cats have 4 legs. legs count must be divisible by 4
    if l%4 != 0 :
        return 'no'
    # max no of cats that can be on dogs
    cats_on_dogs = d*2
    
    cats_must_on_ground = -1
    # considering max possible cats are on dogs remaining cats.
    if c-cats_on_dogs < 1 :
        cats_must_on_ground = 0
    else :
        cats_must_on_ground = c-cats_on_dogs
    min_legs_on_ground = (d*4) + (cats_must_on_ground*4)
    max_legs_on_ground = (d*4) + (c*4)
    # if no of legs on ground are in more than min legs and max legs return no
    if l < min_legs_on_ground or l > max_legs_on_ground:
        return 'no'
    else :
        return 'yes'

print(validate_leg_count(1,1,12))