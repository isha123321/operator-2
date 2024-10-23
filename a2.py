height=float(input("enter your height in m:"))
weight=float(input("enter your weight in kg:"))
bmi=weight/(height**2)
print("your bmi is",bmi)
if bmi <=18.5:
    print("you are underweight")
elif bmi >18.5 and bmi <=24.9:
    print("you are healthy")    
elif bmi >=24.9 and bmi <=29.9:
    print("you are over weight")
else:
    print("you are obease")    


