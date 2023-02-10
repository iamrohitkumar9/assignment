
# Question 1

p=int(input("Enter the percentage : "))
if p>90:
    print("Grade A")
elif p>80 and p<=90:
    print("Grade B")
elif p>=60 and p<=80 :
    print("Grade C")
else :
    print("Grade D")


# Question 2

cp=int(input("Enter the cost price of a bike : "))
if cp >100000:
    tax=(15/100)*cp
    print(tax)
elif cp >50000 and cp<=100000 :
    tax=(10/100)*cp
    print(tax)
else:
    tax=(5/100)*cp
    print(tax)


# Question 3

city=input("Enter the city : ")
if city =="Delhi":
    print("Red Fort")
elif city=="Agra":
    print("Taj Mahal")
elif city=="Jaipur":
    print("Jal Mahal")


# Question 4

count = 0
num = int(input("Enter a number: "))
while num > 10:
    num /= 3
    count += 1
print("The number can be divided by 3", count, "times before it is less than or equal to 10.")


# Question 5

# The while loop in C is used to evaluate a test condition and iterate over the loop body until the condition returns True.
# Use of while loop for printing from 1 to given number n .

n=int(input("Enter a number : "))
i=1
while i<=n:
    print(i)
    i+=1


# Question 6
# Nested Loop to print 3 different pattern

# Pattern 1

i = 0
while i < 5:
    j = 0
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1


# Pattern 2


i = 5
while i > 0:
    j = 0
    while j < i:
        print("*", end=" ")
        j += 1

    print()

    i -= 1

# Pattern 3

i = 5
while i > 0:
    j = 5
    while j > 0:
        if (j > i):
            print(" ", end=" ")

        else:

            print("*", end=" ")

        j -= 1

    print()
    i -= 1


# Question 7 and Question 8 are same ...

i=10

while i>=1:
    print(i)
    i-=1

