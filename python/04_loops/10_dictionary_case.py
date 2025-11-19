users = [
    {"id":1,"total": 100,"coupon":"P20"},
    {"id":2,"total": 150,"coupon":"P30"},
    {"id":3,"total": 50,"coupon":"P50"},
]

discounts = {
    "P20": (0.2,0),
    "P30": (0.5,0),
    "P50": (0,10),
}

for user in users:
    percent,fixed = discounts.get(user["coupon"],(0,0))
    print(f"percent : {percent}")
    print(f"fixed : {fixed}")
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user['total']} and got discount for next visit of rs {discount}")