def average(a, b):
    return (a + b) / 2


def double(number):
    return number * 2


try:
    age = int(input("Age: "))
except ValueError:
    print("Invalid input. Please enter a valid integer for age.")
except:  
    pass

def calculate_grade(mark):
    if mark >= 85:
        return "A"
    elif mark >= 70:
        return "B"
    else:
        return "below B"


ali_mark = 88
sara_mark = 73
hamza_mark = 62

print("Ali:", calculate_grade(ali_mark))
print("Sara:", calculate_grade(sara_mark))
print("Hamza:", calculate_grade(hamza_mark))