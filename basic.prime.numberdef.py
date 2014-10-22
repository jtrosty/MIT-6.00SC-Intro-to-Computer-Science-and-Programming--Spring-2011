def is_prime(x):
    count = 2
    if x == 1 or x <=0:
        return False
    elif x == 2:
        return True
        
    while count < x:
        if (x % count) == 0:
            return False
            break
        elif (count == x-1):
            return True
        else:
            count += 1
            
        
        
print is_prime(11)
