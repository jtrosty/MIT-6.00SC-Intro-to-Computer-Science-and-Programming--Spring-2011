# 6.00 Problem Set 2
#
# Successive Approximation
###
##poly = (0.0, 0.0, 5.0, 9.3, 7.0)
##poly2 = (-13.39, 0.0, 17.5, 3.0, 1.0) 

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    x = x
    exp = 0
    ans = 0.0 # this will be my answer
    for i in poly:
        ans += i*(x**exp)
        exp += 1
        #print ans
    return ans

#print evaluate_poly(poly,-13)
    
    # TO DO ... 


def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    # TO DO ...
    deriv = []
    exp = 0
    b = 0.0
    for i in poly:
        b = exp * i
        deriv.append(b)
        exp += 1
        #print ans
    del deriv[0]    
    return deriv

poly = (-13.39, 0.0, 17.5, 3.0, 1.0)

def evaluate_deriv(poly, x):
    # takes a poly nomial, uses the compute_deriv function to
    # get it's derivative poly then evaluate it for x
    return evaluate_poly(compute_deriv(poly),x)

def compute_root(poly, x_0, epsilon):
    # finds the root of a poly nomial function using newton's method
    # only will find 1 root at a time and stop. 
    
    y = evaluate_poly(poly, x_0)
    x_old = x_0
    i = 0
    y_prim = 0.0
    
    while abs(y) >= epsilon: 
        y = evaluate_poly(poly, x_old)
        y_prim = evaluate_deriv(poly, x_old)
        
        x_new = x_old - (y/y_prim)
        
        x_old = x_new
        i += 1
        print 'y is: ', y
        print 'x_new is: ', x_new

    return (x_new, i)

print compute_root(poly, -120, 0.0001)

    
    # TO DO ... 

##def findRoot(pwr, val, epsilon):
##"""assumes pwr an int; val, epsilon floats
##pwr and epsilon > 0
##if it exists,
##returns a value within epsilon of val**pwr
##otherwise returns None""" 
##    assert type(pwr) == int and type(val) == float\
##    and type(epsilon) == float
##    assert pwr > 0 and epsilon > 0
##    if isEven(pwr) and val < 0:  return None 
##    low = -abs(val)
##    high = max(abs(val), 1.0)
##    ans = (high + low)/2.0
##    while not withinEpsilon(ans**pwr, val, epsilon):
##            #print 'ans =', ans, 'low =', low, 'high =', high
##        if ans**pwr < val:
##            low = ans 
##        else: 
##            high = ans
##            ans = (high + low)/2.0
##        return ans 

