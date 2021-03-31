def get_gross_salary(salary) :
    hra = 0
    da = 0
    if salary < 1500 :
        hra = salary*.1
        da = salary*0.9
    else :
        hra = 500
        da = salary*0.98
    return salary+hra+da

print(get_gross_salary(1312))