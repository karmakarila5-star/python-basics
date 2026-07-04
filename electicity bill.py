unit = int(input("please enter number os units consumed : "))
if (unit < 50) :
    amount = unit * 2.60
    surcharge = 25
elif (unit <=100):
    amount = 130 + ((unit - 50) * 3.25)
    surcharge = 35
elif (unit <= 200):
    amount = 130 + 162.50 * ((unit- 100) * 5.26)
    surcharge = 45
else:
    amount = 130 + 162.50 + ((unit - 200) * 8.45)
    surcharge = 75
total  = amount + surcharge
print("\nelectricity bill = %.2f" %total)

