num1=int(input("ENTER NUMBER 1:"))
num2=int(input("ENTER NUMBER 2:"))
entered_char=input("\n ENTER 1 FOR ADD \n ENTER 2 FOR SUBTRACT \n ENTER 3 FOR MULTIPLY \n ENTER 4 FOR DIVISION \n ENTER 5 FOR FLOOR DIVISION \n ENTER 6 FOR MODULUS \n ENTER 7 FOR EXPONENT \n")
if(entered_char=='1'):
    print("ADDITION OF NUM1 AND NUM2:",num1+num2)

if(entered_char=='2'):
    print("SUBTRACTION OF NUM1 AND NUM2:",num1-num2)

if(entered_char=='3'):
    print("MULTIPLY OF NUM1 AND NUM2:",num1*num2)

if(entered_char=='4'):
    print("DIVISION OF NUM1 AND NUM2:",num1/num2)

if(entered_char=='5'):
    print("FLOOR DIVISION OF NUM1 AND NUM2:",num1//num2)

if(entered_char=='6'):
    print("MODULUS OF NUM1 AND NUM2:",num1%num2)

if(entered_char=='7'):
    print("EXPONENT OF NUM1 AND NUM2:",num1**num2)

print("-----END OF THE CODE-----")