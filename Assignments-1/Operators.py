#1. Perform addition, subtraction, multiplication, and division.
print("==============1===============")
A=int(input("Enter Number:- "))
B=int(input("Enter Number:- "))
print("Addition:- ",A+B)
print("Subtraction:- ",A-B)
print("Multiplication:- ",A*B)
print("Division:- ",A/B)

#2. Find the remainder and quotient of two numbers.
print("==============2===============")
dividend = 15
divisor = 4
quotient = dividend // divisor
remainder = dividend % divisor
print("Quotient:", quotient)    
print("Remainder:", remainder)

#3. Check whether a number is even or odd.
print("==============3===============")
A=int(input("Enter Number:- "))
if A%2==0:
    print("EVEN")
else:
    print("ODD")
    
#4. Compare two numbers using relational operators.
print("==============4===============")
A=int(input("Enter Number 1:- "))
B=int(input("Enter Number 2:- "))
if A==B:
    print("Both Are Equal")
else:
    print("Both Are Not Equal")
    
#5. Demonstrate logical operators (and, or, not).
print("==============5===============")
a = True
b = False
print(a and b)#=> True And False = False
print(a or b)#=> True Or False = True
print(not a)#=> Not True = False0

#6. Demonstrate assignment operators (+=, -=, *=, /=).
print("==============6===============")
a = 10
b = 10
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b /= a
print(b)

#7. Find the largest of two numbers using comparison operators.
print("==============7===============")
A=int(input("Enter Number 1:- "))
B=int(input("Enter Number 2:- "))
if A<B:
    print(B,"Is Big")
else:
    print(A,"Is Big")

    
