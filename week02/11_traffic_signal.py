density=input("Enter Density(Low, Medium, high): ")
e_vehicle=input("Emergency Vehicle Is Present?(Yes/No): ")

if density == "low":
    time = 20
elif density == "medium":
    time = 40
elif density == "high":
    time = 60
else:
    print("Invalid density")
    time = 0

if time != 0:
    if e_vehicle == "yes":
        print("Emergency override: route receives immediate green.")
    else:
        print("Green light time:", time, "seconds")