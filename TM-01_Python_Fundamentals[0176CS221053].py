'''           EXERCISES           '''

#Write a program to check if a given number is Positive, Negative or Zero.

print("check if number is positive, negative or zero")
a = float(input("enter a number: "))
if a < 0:
    print("negaative number")
elif a > 0:
    print("positive number")
else:
    print("zero")

#Write a program to check if a given number is odd or even.

print("\nodd or even check")
a = int(input("enter a number: "))
if a % 2 == 0:
    print("even number")
else:
    print("odd number")

#Given two non-negative values, print true if they have the same last digit, such as with 27 and 57

print("\nchecks if two numbers have same last digit")
a = int(input("enter a number: "))
b = int(input("enter other number: "))
print(a % 10 == b % 10)

#Write a program to print numbers from 1 to 10 in a single row with one tab space.

print("\nnumbers from 1 to 10 in a single row with one tab space")
for i in range(1, 11):
    print(i, end='\t')

#Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.

print("\n\neven numbers between 23 and 57")
for i in range(23, 58):
    if i % 2 == 0:
        print(i)

#Write a program to check if a given number is prime or not.

print("\ncheck if number is prime or not")
def prime_check(n):
    if n <= 1:
        return "not prime"
    if n == 2:
        return "prime number"
    if n % 2 == 0:
        return "not prime"
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return "not prime"
    return "prime number"
a = int(input("enter a number: "))
print(prime_check(a))

#Write a program to print prime numbers between 10 and 99.

print("\nprime numbers between 10 and 99")
for n in range(10, 100):
    if n % 2 == 0:
        continue
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            break
    else:
        print(n)

#Write a program to print the sum of all the digits of a given number.

print("\ncalculate sum of all digits of number")
a = int(input("enter a number: "))
res = 0
while a > 0:
    res += a % 10
    a //= 10
print(res)

#Write a program to reverse a given number and print.

print("\nreverse a number")
a = int(input("enter a number: "))
res = 0
while a > 0:
    rem = a % 10
    res = (res * 10) + rem
    a //= 10
print(res)

#Write a program to find if the given number is palindrome or not.

print("\ncheck if number is palindrome or not")
a = int(input("enter a number: "))
temp = a
rev = 0
while temp > 0:
    rem = temp % 10
    rev = (rev * 10) + rem
    temp //= 10
if rev == a:
    print("palindrome")
else:
    print("not palindrome")

'''-------------------------------------------------------------------------------------------------------------------------------------------------'''

#             MINI PROJECT
'''
create a python program that asks the user how far they want to travel. if they want to travel less than three
miles tell them to ride Bicycle. if they want to travel more than three miles, but less than three hundred
miles, tell them to ride Motor-cycle. if they want to travel three hundred miles or more tell them to drive
Super-Car.

Sample Output:

How far would you like to travel in miles? 2500

I suggest Super-Car to your destination
'''
print("\nmini project 1: vehicle recommendation")
dist = float(input("How far would you like to travel in miles? "))
if dist == 0:
    print("You don't need to Travel.")
elif dist > 0:
    if dist < 3:
        print("I suggest Bicycle to your destination.")
    elif 3 <= dist <300:
        print("I suggest Motor-cycle to your destination.")
    else:
        print("I suggest Super-Car to your destination.")
else:
    print("Enter valid Distance!")

'''
Let's assume you are planning to use your python skills to build an App for Mobile.

You decide to host your application on servers running in the cloud. you pick a hosting provider that charges
$0.51 per hour. you will launch your services using one server and want to know how much it will cost to
operate per day, per week, per month.

Write a python program that displays the answers to the following questions:

How much does it cost to operate one server per day?

How much does it cost to operate one server per week?

How much does it cost to operate one server per month?

How much days can I operate one server with $918?
'''
print("\nmini project 2: cloud server hosting charges")
phc = 0.51
pdc = phc * 24
pwc = pdc * 7
pmc = pdc * 30
print(f"How much does it cost to operate one server per day?\n${pdc}")
print(f"How much does it cost to operate one server per week?\n${pwc}")
print(f"How much does it cost to operate one server per month?\n${pmc}")
print(f"How much days can I operate one server with $918?\n{int(918/pdc)} days")


'''
Submitted by:
Ayush Kumar Sinha
0176CS221053
'''
