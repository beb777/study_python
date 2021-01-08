def computepay(h,r):
    if h<=40:
        payment=h*r
        return payment
    else:
        payload=(40*r)+((h-40)*1.5*r)
        return payment

h=float(input('Enter Hours:'))
r=float(input('Enter Rate:'))

pay=computepay(h,r)

print(pay)