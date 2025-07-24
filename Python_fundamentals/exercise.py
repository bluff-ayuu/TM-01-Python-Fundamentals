'''           EXERCISES           '''

#1. Write a program to check if a given number is Positive, Negative or Zero.

print("check if number is positive, negative or zero")
a = float(input("enter a number: "))
if a < 0:
    print("negaative number")
elif a > 0:
    print("positive number")
else:
    print("zero")

#2. Write a program to check if a given number is odd or even.

print("\nodd or even check")
a = int(input("enter a number: "))
if a % 2 == 0:
    print("even number")
else:
    print("odd number")

#3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57

print("\nchecks if two numbers have same last digit")
a = int(input("enter a number: "))
b = int(input("enter other number: "))
print(a % 10 == b % 10)

#4. Write a program to print numbers from 1 to 10 in a single row with one tab space.

print("\nnumbers from 1 to 10 in a single row with one tab space")
for i in range(1, 11):
    print(i, end='\t')

#5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.

print("\n\neven numbers between 23 and 57")
for i in range(23, 58):
    if i % 2 == 0:
        print(i)

#6. Write a program to check if a given number is prime or not.

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

#7. Write a program to print prime numbers between 10 and 99.

print("\nprime numbers between 10 and 99")
for n in range(10, 100):
    if n % 2 == 0:
        continue
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            break
    else:
        print(n)

#8. Write a program to print the sum of all the digits of a given number.

print("\ncalculate sum of all digits of number")
a = int(input("enter a number: "))
res = 0
while a > 0:
    res += a % 10
    a //= 10
print(res)

#9. Write a program to reverse a given number and print.

print("\nreverse a number")
a = int(input("enter a number: "))
res = 0
while a > 0:
    rem = a % 10
    res = (res * 10) + rem
    a //= 10
print(res)

#10. Write a program to find if the given number is palindrome or not.

print("\ncheck if number is palindrome or not")
a = int(input("enter a number: "))
temp = a
rev = 0
while temp > 0:
    rem = temp % 10
    rev = (rev * 10) + rem
    temp //= 10
if rev == a:
    print(f"{a} is palindrome")
else:
    print(f"{a} is not palindrome")


'''
Submitted by:
Ayush Kumar Sinha
0176CS221053
DS_251120024
'''
