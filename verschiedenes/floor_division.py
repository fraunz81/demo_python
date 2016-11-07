def digit_sum(x):
	total = 0
	tmp = x
	digit = 0
	while tmp > 0:
		digit = tmp % 10
		tmp = tmp // 10
		total += digit
		digit = 0
	
	return total


def digit_sum2(x):
    nStr = str(x)
    total = 0
    for c in nStr:
        total += int(c)
    
    return total


print(digit_sum(1234))
	
