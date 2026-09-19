#1. Check whether a number is positive, negative, or zero.
print("=======================1=======================")
A=int(input("Enter Number:- "))
if A<0:
        print("Number is Nagetive")
elif A>0:
         print("Number is Positive")
else:
     print("Number is Zero")
     
#2. Check whether a person is eligible to vote.
print("=======================2=======================")
A=int(input("Enter Your Age:- "))
if A>=18:
        print("You Are Eligible For Vote")
else:
     print("You Are Not Eligible For Vote")
     
#3. Find the largest of three numbers.
print("=======================3=======================")
A=int(input("Enter Number:- "))
B=int(input("Enter Number:- "))
C=int(input("Enter Number:- "))
if A>B and A>C:
                print(A,"Is Big")
elif A<B and B>C:
                 print(B,"Is Big")
else:
     print(C,"Is Big")

#4. Check whether a year is a leap year.
print("=======================4=======================")
A=int(input("Enter Year:- "))
if A%4==0:
        print("It Is Leap Year")
else:
   print("It Is  Not Leap Year")
   
#5. Create a grade system based on marks.
print("=======================5=======================")
marks=float(input("Enter your Number: "))
if marks >= 90:
       Grade= "A"
elif marks >= 80:
        Grade= "B"
elif marks >= 70:
        Grade= "C"
elif marks >= 60:
       Grade= "D"
else:
        Grade= "F"
print("Grade=",Grade)

#6. Check whether a number is divisible by 5 and 11.
print("=======================6=======================")
A=int(input("Enter Number:- "))
if A%5==0 and A%11==0:
                    print("Number is Dvided By 5 And 11")
else:
     print("Number is Not Dvided By 5 And 11")
     
#7. Create a simple calculator using if-elif-else.
print("=======================7=======================")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Available operators: +, -, *, /")
operator = input("Enter an operator: ")

if operator == '+':
    result = num1 + num2
    print("Result:",result)

elif operator == '-':
    result = num1 - num2
    print("Result:", result)

elif operator == '*':
    result = num1 * num2
    print("Result:", result)

elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid operator! Please use +, -, *, or /.")
