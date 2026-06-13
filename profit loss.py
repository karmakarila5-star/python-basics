actual_cost = float(input("please enter the actual product price: "))
sale_price = float(input("please enter the sales amount:"))
if (sale_price > actual_cost):
    amount = sale_price - actual_cost
    print("total profit = {0}".format(amount))
else:
    print("no profit!!!")