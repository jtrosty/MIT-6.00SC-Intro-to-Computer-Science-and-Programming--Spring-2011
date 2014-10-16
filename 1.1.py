principal = raw_input("What is the outstanding balance on your card? ")
interest_rate = raw_input("Your anual interest rate? ")
monthly_payment = raw_input("your monthy payment as a decimal? ")
w = float(principal)
y = float(interest_rate) 
z = float(monthly_payment)
x = 0.0
x = w*y
print x

def monthly_pay(prin, rate, payment):
    i = 1
    paid = 0.0
    balance = prin
    while i < 13:
        print 'Month'+ str(i)
        pay = payment * balance
        paid += pay
        print 'Minimum monthly payment: $' + str(round(pay,2))
        interest = (rate/12) * balance
        pay = pay- interest
        print 'Principle paid: $' + str(round(pay,2))
        balance = balance - pay
        print 'Remaining balance: $' + str(round(balance,2))
        i +=1
    print "RESULTS"
    print "total amount paid", round(paid,2)
    print "remainig blance", round(balance,2) 


monthly_pay(w, y, z)

