# device_status = input("Is Device is Active or off: ").lower()
device_status = "active"
temp = 30

if device_status == "active":
#    temp=  int(input("what is your romm temperature: "))
   if temp > 35:
       print("Warn! High Temprature")
   else: 
       print("Temprature Normal")
else :
    print("Device is Offline")