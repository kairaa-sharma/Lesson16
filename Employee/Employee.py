def employee(name):
    print(name)

def salary(exp):
    if exp>=5:
        return 300,000
    elif exp>=3:
        return 100,000
    else:
        return 500,000
employee("Ram")
a = salary(15)
print("The salary of the employee is", a)
