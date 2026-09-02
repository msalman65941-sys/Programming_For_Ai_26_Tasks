usd = float(input("Enter amount in USD: "))
exchange_rate = float(input("Enter exchange rate: "))

local_currency = usd * exchange_rate

print("Converted amount =", round(local_currency, 2))