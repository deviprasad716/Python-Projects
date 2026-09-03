weight=float(input("Enter your weight: "))
unit=input("(L)bs or (K)g: ")

if unit.lower()=='l':
    converted_weight=weight*0.45
    print(f"You are {converted_weight} kgs..")
else:
    converted_weight=weight/0.45
    print(f"You are {converted_weight} pounds..")
