def checker(result):
    if result.is_integer():
        return int(result)
    return result
def calculater(a,b,symbol ):
    if symbol=='+':
        result=a+b
        result=checker(result)
        return "Addition is:",result
    elif symbol=='-':
        result=a-b
        result=checker(result)
        return "Subraction is:",result
    elif symbol=='*':
        result=a*b
        result=checker(result)
        return "Multiplication is:",result
    elif symbol=='/':
        result=a/b
        if result.is_integer():
            return "Division is:",int(result)
        else:
            return "Division is:",f"{result:.2f}"
        
    elif symbol=='%':
        result=a%b
        result=checker(result)
        return "Modulo is:",result
    else:
        return "Enter valid Symbol"
a=float(input("Enter the 1st Number:"))
b=float(input("Enter the 2nd Number:"))
symbol=input("Enter the Operator:")
print(*calculater(a,b,symbol))
