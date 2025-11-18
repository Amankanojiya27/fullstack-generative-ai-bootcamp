seat_type = input("Enter Seat type (sleeper/AC/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds availabe")
    case "ac":
        print("AC - Air conditioned, comfy ride")
    case "general":
        print("General- Cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seat with meals")
    case _:
        print("Invaild seat type")
