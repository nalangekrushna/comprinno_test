def get_ship_type(id) :
    # lowercase the id.
    id = id.lower()
    if id == 'b' :
        return 'BattleShip'
    elif id == 'c' :
        return 'Cruiser'
    elif id == 'd' :
        return 'Destroyer'
    elif id == 'f' :
        return 'Frigate'
    else :
        return 'please give right type of id.'

print(get_ship_type('B'))