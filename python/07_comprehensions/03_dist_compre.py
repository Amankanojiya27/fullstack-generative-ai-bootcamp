# Dictionary Comprehensions in Python
tea_prices_inr = {
    "Masala Chai":40,
    "Green Chai":30,
    "Lemon Chai":200,
}
# -------------------------------------
#      Syntax - [expression for item in iterable if condition]
#                    |             |         |       |  |
#                  key:value
#                    |
tea_prices_usd = { tea:price/80 for tea, price in tea_prices_inr.items()}

print(tea_prices_usd)