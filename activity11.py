#conditional statements 
#Ask user to input a temperature
#conditions as follow: 
# below 0 Freezing Temperature
# 1 - 20 -- Extremely Cold
# 21 to 30 -- Moderatelyt
# 31 to 37 -- Lukewarm
# 38 to 45 -- Hot
# 45 to 50 -- Boiling Hot
# 51 and above -- Dangerous Temperature

temp = eval(input("Enter Temperature outside --> "))
#input 33

if temp >= 1 and temp <= 28:
             print("Temperature is Considered as Extremely Cold")

elif temp >= 21 and temp <= 30:
             print("Temperature is Considered as Moderatelyt")

elif temp >= 38 and temp <= 45:
             print("Temperature is Considered as Moderatelyt")
else:
             print("Invalid Temperature")