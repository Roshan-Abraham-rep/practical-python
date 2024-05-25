# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
num_months = 0
extra_payment_start_month = 1
extra_payment_end_month = 12
extra_payment = 1000

while principal > 0:
    num_months = num_months + 1
    if num_months >= extra_payment_start_month and  num_months <= extra_payment_end_month:
        principal = principal * (1+rate/12) - payment + extra_payment
    else:
        principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    
print('Total paid', total_paid)
print('Num of months', num_months)

