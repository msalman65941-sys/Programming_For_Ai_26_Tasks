food_price = float(input("Enter food price: "))
tax_percentage = float(input("Enter tax percentage: "))
discount_percentage = float(input("Enter discount percentage: "))
service_charge = float(input("Enter fixed service charge: "))

# 1. Add tax
amount_after_tax = food_price + (food_price * tax_percentage / 100)

# 2. Subtract discount
amount_after_discount = amount_after_tax - (amount_after_tax * discount_percentage / 100)

# 3. Add service charge
final_bill = amount_after_discount + service_charge

# 4. Display final bill
print("Final bill =", f"{final_bill:.2f}")