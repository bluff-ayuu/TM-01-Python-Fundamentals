#Q1)Write a program to read the entire content from a txt file and display it to the user.

fn = input("Enter the filename: ")
with open(fn, 'r') as f:
    c = f.read()  
    print("\n--- File Content ---")
    print(c)

#Q2)Write a program to read first lines from a txt file. Get n as user input.

fn = input("Enter the filename: ")
n = int(input("Enter the number of lines to read: "))
with open(filename, 'r') as f:
    print(f"\n--- First {n} lines ---")
    for i in range(n):
        l = f.readline()
        if not l:
            break  
        print(l.strip())  

#Q3)Write a program to accept Input from user and append it to a txt file.

fn = input("Enter the filename: ")
text = input("Enter the text you want to append: ")
with open(fn, 'a') as f:
    f.write(text + '\n')
print("Text has been appended to the file successfully.")

#Q4)Write a program to read contents fron a txt file line by line and store each line into a list.

fn = input("Enter the filename: ")
lines = []
with open(fn, 'r') as f:
    for l in f:
        lines.append(l.strip()) 
print("Lines stored in the list:")
print(lines)

#Q5)Write a program to find the longest word from the txt file contents, assuring that the file will have only one longest word in it.

fn = input("Enter the filename: ")
lword = ""
with open(fn, 'r') as f:
    for l in f:
        words = l.split()  
        for w in words:
            if len(w) > len(lword):
                lword = w
print("The longest word in the file is:", lword)

#Q6)Write a program to count the frequency of a user entered word in a txt file.

fn = input("Enter the filename: ")
word = input("Enter the word to search: ")
c = 0
with open(fn, 'r') as f:
    for l in f:
        words = l.split()
        for w in words:
            if w.strip('.,!?').lower() == word.lower():
                c += 1
print(f"The word '{word}' appears {c} time(s) in the file.")
