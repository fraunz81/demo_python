def factorial(x):
	if x <= 1:
		return 1
	
	return x * factorial(x-1)


def factorial2(x):
    total = 1
    for i in range(1, x+1):
        total *= i
    
    return total



print(factorial(4))
