#1. Write a function to print "Hello, World!".
print("=======================1=======================")

def Hello():
            print("Welcome To The DSA ")
Hello()

#2.Write a function that takes a name and prints a greeting.
print("=======================2=======================")

def Greeting(name):
    print("Hello: ",name)
Greeting('Sanjana')

#3.Write a function to add two numbers.
print("=======================3=======================")

def Addition(A,B):
    print("Addition Is: ",A+B)
Addition(5,5)

#4.Write a function to find the square of a number.
print("=======================4=======================")

def Square(A):
             print("Square: ",A*A)
Square(2)
             
#5.Write a function to check whether a number is even or odd.
print("=======================5=======================")

def check(a):
                if a%2==0:
                            print("This numer is Even")
                else:
                            print("This number is Odd")
check(7)
            
#6.Write a function to find the maximum of two numbers.
print("=======================6=======================")

def find(a,b):
            if a>b:
                  print("A is Max then B")
            else:
                 print("B is MAx then A")
find(4,5)

#7.	Write a function to convert Celsius to Fahrenheit.
print("=======================7=======================")

def convert(c):
    print((c * 9/5) + 32)

convert(25)

#8. Write a function to calculate the area of a circle.
print("=======================8=======================")

def area(r):
    print("Area =", 3.14 * r * r)

area(5)

#9. Write a function to calculate the factorial of a number.
print("=======================9=======================")

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    print("Factorial =", f)

factorial(5)

#10. Write a function to check whether a number is positive, negative, or zero.
print("=======================10=======================")

def check(n):
    if n > 0:
        print("Number is Positive")
    elif n < 0:
        print("Number is Negative")
    else:
        print("Number is Zero")

check(5)

#11. Write a function to find the maximum of three numbers.
print("=======================11=======================")

def maximum(a, b, c):
    if a > b and a > c:
        print("A is Maximum")
    elif b > a and b > c:
        print("B is Maximum")
    else:
        print("C is Maximum")

maximum(4, 8, 6)

#12. Write a function to count vowels in a string.
print("=======================12=======================")

def count_vowels(s):
    count = 0
    for i in s:
        if i in "aeiouAEIOU":
            count = count + 1
    print("Number of Vowels =", count)

count_vowels("hello")

#13. Write a function to reverse a string.
print("=======================13=======================")

def reverse(s):
    print("Reverse =", s[::-1])

reverse("hello")

print("14.-----------")

def palindrome(s):
    if s == s[::-1]:
        print("String is Palindrome")
    else:
        print("String is Not Palindrome")

palindrome("madam")

#14. Write a function to check whether a string is a palindrome.
print("=======================14=======================")

def palindrome(s):
    if s == s[::-1]:
        print("String is Palindrome")
    else:
        print("String is Not Palindrome")

palindrome("madam")

#15. Write a function to find the sum of all elements in a list.
print("=======================15=======================")

def sum_list(a):
    total = 0
    for i in a:
        total = total + i
    print("Sum =", total)

sum_list([1, 2, 3, 4, 5])

#16.Write a function to find the largest element in a list.
print("=======================16=======================")

def largest(a):
    max = a[0]

    for i in a:
        if i > max:
            max = i

    return max

a = [10, 20, 5, 30, 15]
print(largest(a))
#17.	Write a function to remove duplicate elements from a list.
print("=======================17=======================")

def remove_dup(a):
    b = []

    for i in a:
        if i not in b:
            b.append(i)

    return b

a = [1, 2, 2, 3, 3, 4]
print(remove_dup(a))

#18.	Write a function to count how many times an element appears in a list.
print("=======================18=======================")

def count(a, n):
    c = 0

    for i in a:
        if i == n:
            c = c + 1

    return c

a = [1, 2, 2, 3, 2, 4]
print(count(a, 2))
#19.Write a function to check whether a number is prime.
print("=======================19=======================")

def prime(n):
    c = 0

    for i in range(1, n + 1):
        if n % i == 0:
            c = c + 1

    if c == 2:
        return True
    else:
        return False

n = 7
print(prime(n))

#20.	Write a function to return all prime numbers between two numbers.
print("=======================20=======================")

def primes(a, b):
    for n in range(a, b + 1):
        c = 0

        for i in range(1, n + 1):
            if n % i == 0:
                c = c + 1

        if c == 2:
            print(n)

primes(10, 30)

#21.	Write a function to calculate Fibonacci numbers.
print("=======================21=======================")

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c

fibonacci(7)

#22.Write a function to find the second-largest number in a list.
print("=======================22=======================")

def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)

numbers = [10, 5, 8, 20, 15]
print("Second large number =",second_largest(numbers))

#23.Write a function to sort a list without using sort().
print("=======================23=======================")

def sort_list(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

numbers = [5, 2, 8, 1, 3]

#24.Write a function to merge two lists and remove duplicates.
print("=======================24=======================")

def merge_lists(list1, list2):
    return list(set(list1 + list2))

print("Final list =" ,merge_lists([1, 2, 3], [3, 4, 5]))

#25.Write a function that accepts any number of arguments using *args.
print("=======================25=======================")

def add_numbers(*args):
    return sum(args)

print("Args =",add_numbers(1, 2, 3, 4, 5))

#26.Write a function that accepts keyword arguments using **kwargs.
print("=======================26=======================")

def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_details(name="Alice", age=25, city="Delhi")

#27.Write a recursive function to calculate factorial.
print("=======================27=======================")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial = ",factorial(5))

#28.	Write a recursive function to calculate the sum of numbers from 1 to n.
print("=======================28=======================")

def sum_to_n(n):
    if n <= 0:
        return 0
    return n + sum_to_n(n - 1)

print("Sum =", sum_to_n(5))

#29.	Write a function to find the frequency of each word in a sentence.
print("=======================29=======================")

from collections import Counter

def word_frequency(sentence):
    words = sentence.lower().split()
    return Counter(words)

print(word_frequency("hello world hello"))

#30.Write a function to determine whether two strings are anagrams.
print("=======================30=======================")

def are_anagrams(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    return sorted(s1) == sorted(s2)

print(are_anagrams("listen", "silent"))


