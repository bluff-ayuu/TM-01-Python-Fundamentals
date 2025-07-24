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
DS_251120024
'''
