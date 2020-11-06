#Choose a list of your choice and find the sum of all elements of that list.
num=[2,5,8,9,10,22,30]
sum=0
for i in num:
    sum=sum+i

print("The total sum of the list (", num ,") is :", sum)

print("*"*20)

#Write a program that returns a list which contains common elements from two lists. Avoid
#the duplicate elements from lists
a=[10,12,2,44,6,1,0,55]
b=[22,15,3,12,0,6,8,1]

a_set=set(a)
b_set=set(b)

common=list(a_set.intersection(b_set))
print("The common elements from: ")
print(a_set)
print(b_set)
print("-"*15)
print(list(common))

print("*"*20)

#Print each number using loop.
#Also, print the square of each number using loop

num=[2,4,6,8,10,12]
print("The numbers are: ")
for i in num:
    print(i, end=" ")
print("\nThe square of the numbers are: ")
for i in num:
    print(i**2, end=" ")

print(" ")
print("*"*20)

#Write a code to ask an input from the user which is a string and display the string along
#with its length.

string=input("Please enter a string:")
count=0
for i in string:
    count=count+1

print("The string you entered is:",string ,"and its length is: ", count)

print("*"*20)
#Write a code to ask an input from the user which is a string and convert it to uppercase
#and lowercase.

string=input("Please enter any lines for us:")
print("-"*15)
print("The line you wrote:",string)
print("-"*15)
print("The line in uppercase: ",string.upper())
print("The line in lowercase: ", string.lower())