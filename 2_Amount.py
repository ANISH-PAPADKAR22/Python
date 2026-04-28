#To calculate profit or loss
cost_price=int(input("Enter the cost price:"))
selling_price=int(input("Enter the selling price:"))
if selling_price>cost_price:
    profit=selling_price-cost_price
    print("The profit is:",profit)
elif selling_price<cost_price:
    loss=cost_price-selling_price
    print("The loss is:",loss)
else:
    print("No profit or loss")
'''
Output:-
Enter the cost price:50
Enter the selling price:75
The profit is: 25
'''