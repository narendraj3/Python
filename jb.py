import math
principal = int(input("enter the credit principal:"))
ask = input("what do you want to calculate? type 'm' - for count of months, type 'p' - for monthly payment: \n")
if ask == 'm':
    monthly_payment = int(input("enter monthly payment:"))
    payment = principal/monthly_payment
    j = math.ceil(payment)
    print("It takes {} month to repay the credit".format(j))
if ask =='p':
    months = int(input("enter count of months:"))
    paymen = principal/months
    r = math.ceil(paymen)
    print(r)
    lastpayment = principal-(months-1)*r
    print("Your monthly payment= {} with last payment= {}".format(r,lastpayment))



