daily_sales= [5,10,12,15,6,26,47,22]

total_cup = (sale for sale in daily_sales if sale > 30) # <generator object <genexpr> at 0x0000021B8D889490>
total_cup_2 = [sale for sale in daily_sales if sale > 10] # [12, 15, 26, 47, 22]
total_cup_3 = sum(sale for sale in daily_sales if sale > 10) # 122

print(total_cup)
print(total_cup_2)
print(total_cup_3)