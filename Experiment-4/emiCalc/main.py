



def calculate_payment(principal, rate, term):
    r = rate / 1200
    payment = (principal * r) / (1 - (1 + r) ** (-12 * term))
    total_payment = payment * 12 * term
    return payment, total_payment

loan_amount = float(input("Enter loan amount: "))
loan_period = int(input("Enter loan period in years: "))

for i in range(5 * 8, 9 * 8 + 1, 8):
    rate = i / 100
    payment, total_payment = calculate_payment(loan_amount, rate, loan_period)
    print(f"Interest rate: {rate}%")
    print(f"Monthly payment: ${payment:.2f}")
    print(f"Total payment: ${total_payment:.2f}")
    print()
