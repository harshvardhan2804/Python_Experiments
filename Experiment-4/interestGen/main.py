def calculate_monthly_payment(loan_amount, interest_rate, time):
    monthly_interest_rate = interest_rate / 12
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -time)
    return monthly_payment


loan = int(input("enter loan amount:"))
rate = int(input("enter rate of interest:"))
time = int(input("enter the time:"))

monthlyPayment = calculate_monthly_payment(loan,rate,time)

balance = loan

for i in range(1,  time*12+1):
    interest  =  rate*balance
    principal = monthlyPayment - interest
    balance = balance - principal
    print(i, "\t\t", interest, "\t\t",  principal,  "\t\t",balance)
