#1. Demonstrate int, float, str, bool, and complex.
print("==============1===============")
I=20
F=99.99
S="Sanjana"
is_logged_in=True
has_dissconnected=False
C=2+3J
print("Integer Value:- ",I)
print("Float Value:- ",F)
print("String Value:- ",S)
print("Boolean Value:- ",is_logged_in)
print("Complex Value:- ",C)

#2. Accept two numbers and display their data types.
print("==============2===============")
A=int(input("Enter Value 1:- "))
B=float(input("Enter Value 2:- "))
print(type(A))
print(type(B))

#3. Convert a string number into an integer and float.
print("==============3===============")
A="43"
I=int(A)
F=float(A)
print("Stirng Into Integer:- ",int(A))
print("Stirng Into Float:- ",float(A))

#4. Find the length of a string.
print("==============4===============")
A = "Hello, World!"
print("String:- ",A)
Length = len(A)
print('Legnth Is:- ',Length)

#5. Create a list, tuple, set, and dictionary and display their types.
print("==============5===============")
List=["Apple","Banana","Mango","Graps"]
Tuple=("Toyota","Tata","Swift","Honda")
Set={"Hyryder","Puch","I20","Amaze"}
print("List:- ",List)
print(type(List))
print("--------------------------------")
print("Tuple:- ",Tuple)
print(type(Tuple))
print("--------------------------------")
print("Set:- ",Set)
print(type(Set))
