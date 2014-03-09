def recurPower(base, exp):
	if exp == 0:
		return 1
	elif exp == 1:
		return base
	return base*recurPower(base, exp-1)

print recurPower(2, 4)

# Another way to define recurPower

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    
    if exp > 0 and exp%2 == 0:
        return recurPowerNew(base*base, exp/2)
    elif exp > 0:
        return base*recurPowerNew(base, exp-1)
    return 1

print recurPowerNew(2, 4)
