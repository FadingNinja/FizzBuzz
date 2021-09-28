celsius = float(input("Enter your temperature in celsius : "))
fahr = (celsius * 1.8) + 32
if celsius >= 104 :
    print(f"It is hot, the temperature is {fahr} Fahreinheit")
elif celsius <= 50 :
    print(f"It is cold, the temperature is {fahr} Fahreinheit")
else :
    print(f"The temperature is nice, it is {fahr} Fahreinheit") 