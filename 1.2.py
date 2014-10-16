principal = float(raw_input("What is the outstanding balance on your card? "))
interest_rate = float(raw_input("Your anual interest rate? "))

def monthly_pay(prin, rate):
    #amt= prin/12 - ((prin/12)%10) *** for ensuring that it is multiples of 10***
    amt = 10  # problem statement said to start with 10 and only add 10
    bal = prin
    r = rate/12
    i = 0
    
    
    while bal > 0.0:
        bal = bal*(1+r)-amt
        i += 1
        if bal <= 0 and i <13:
            print "Monthly payment to pay off debt in 1 year: ", round(amt,2)
            print "Number of months needed: ", i
            print "Blanace: ", round(bal,2)
        elif i == 13:
            amt = amt + 10
            bal = prin
            i = 0
            
monthly_pay(principal, interest_rate)

