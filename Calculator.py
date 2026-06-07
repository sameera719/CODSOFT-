#simple calculator
print('------Simple Calculator------')
while True:
    print("\nChoose Operations")
    print("+ -> Addition")
    print("- -> Subtraction")
    print("* -> Multiplication")
    print("/ -> Division")
    print("e -> Exit")
    choice=input("Enter Operation(+,-,*,/,e):")
    if choice=='e':
        print("Calculator Closed")
        break
    elif choice in ["+","-","*","/","e"]:
        num1 = float(input("Enter first Number:"))
        num2 = float(input("Enter second Number:"))  
        if choice=='+':
            result=num1+num2
            print(f"Addition({num1},{num2}):",result)
        elif choice=='-':
            result=num1-num2
            print(f"Subtraction({num1},{num2}):",result)
        elif choice=='*':
            result=num1*num2
            print(f"Multiplication({num1},{num2}):",result)
        elif choice=='/':
            if num2 == 0:
                print("Cannot Divide by zero")
            else:
                result=num1/num2
                print(f"Division({num1},{num2}):",result)
    else:
        print("Invalid Choice")
