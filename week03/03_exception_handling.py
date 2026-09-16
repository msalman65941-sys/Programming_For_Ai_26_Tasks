#try:
    #age=int(input("Enter your age: "))
#except ValueError:
    #print("Invalid input. Please enter a valid integer for age.")
#else:
    #print(f"Your age is: {age}")
#finally:
    #print("Execution completed.")

try:
 numerator = float(input("Numerator: "))
 denominator = float(input("Denominator: "))
 result = numerator / denominator
except ValueError:
 print("Enter numeric values only.")
except ZeroDivisionError:
 print("The denominator cannot be zero.")
else:
 print("Result:", result)