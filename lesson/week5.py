def funcname(funcvariable):
    #perform something
    a = 0
    num = []
    for i in range(funcvariable):
        a += i
        num.append(a)
    return num

def multiply(base, step):
    num = base
    if step > 1:
        num += multiply(base, step-1)
    return num

def factorial(num):
    if num < 2:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))