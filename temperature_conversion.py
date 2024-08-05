
def celcius_to_fahrenheit(temp):#this function for celcius to Fahrenheit
    return (temp*9/5)+32
def fahrenheit_to_celcius(temp):#this function for Fahrenheit to Celcius
    return (temp-32)*5/9
temp=float(input("Enter the temperature:"))#get input as Float value
unit=input("Enter the unit (c for celcius and f for fahrenheit):")#get unit as string we can get in single char using [0]
if unit=="c":
    n=celcius_to_fahrenheit(temp)
    print(f"{temp}°C converted to {n:.2f}°F")
elif unit=="f":
    n=fahrenheit_to_celcius(temp)
    print(f"{temp}°F converted to {n:.2f}°C")
else:
    print("Enter valid unit")
#we complete the code now check it
#we completed the task
    