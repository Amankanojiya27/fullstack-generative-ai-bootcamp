def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100


orders = [100,130,150]

for price in orders:
    final_price = add_vat(price,10)
    print(f"Original: {price}, Final with Vat: {final_price}")