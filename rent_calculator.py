## Inputs we need from user
# Total rent
# Total food ordered 
# Electricity units spend
# Charge per unit
# Persons living in villa/flat/room

## Output
# Total amount you have to pay is

rent = int(input(" Enter your hostel/villa/flat rent= "))
food = int(input(" Enter the amount of food ordered = "))
electricity_spend=int(input(" Enter the total electricity spend= "))
charge_per_unit=int(input(" Enter the charge per unit = "))
persons=int(input(" Enter the no of persons living in villa/flat/room = "))

total_bill = electricity_spend * charge_per_unit

output = (food+rent+total_bill) // persons

print("Each person will pay = ", output)