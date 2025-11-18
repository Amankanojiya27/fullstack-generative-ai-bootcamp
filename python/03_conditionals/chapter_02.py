# order_payment = input("Enter the oder amount: ")
order_payment = int(input("Enter the oder amount: "))
print(f"Order amount: {type(order_payment)}")

# part 1
# delivery_fee = 0
# if order_payment > 500:
#     delivery_fee = 0
# else:
#     delivery_fee = 50


# part 2
delivery_fee = 0 if order_payment > 500 else 50

print(f"Delivery Fee is : {delivery_fee}")