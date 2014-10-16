principal = float(raw_input("What is the outstanding balance on your card? "))
interest_rate = float(raw_input("Your anual interest rate? "))

def monthly_pay(prin, rate):
    bal = prin
    r = 1+(rate/12)
    i = 0
    low = 0
    high = (prin*(r)**12)/12
    amt = (high + low)/2
    print amt
    
    while bal > 0.0:
        e = 0.01
        bal = (bal*(r))-amt
       #print "bal", bal
        #print "amt", amt
        i += 1
        if abs(bal) <= 0.01 and i <13:
            print "Monthly payment to pay off debt in 1 year: ", round(amt,2)
            print "Number of months needed: ", i
            print "Blanace: ", round(bal,2)
        elif i == 12 and bal < 0:
            high = amt
            bal = prin
            i = 0
            amt = (high + low)/2
        elif i == 12 and bal > 0:
            low = amt
            bal = prin
            i = 0
            amt = (high + low)/2
            
monthly_pay(principal, interest_rate)

