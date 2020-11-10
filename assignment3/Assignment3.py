#Write a program to display all prime numbers from 1 to 100.

for i in range(1,101):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break

        else:
            print(i)

print("-------------------------------------------------------")

#Ask the user for a string and print out whether this string is a palindrome or not

value=input("Enter a string: ")
reverse=""
for i in range(len(value)-1,-1,-1):
    reverse+=value[i]


if(value==reverse):
    print("The string you entered is palindrome!!!!")
else:
    print("The string you entered is not palindrome")

print("-------------------------------------------------------")

#Given a string, count all lower case, upper case, digits and special symbols.

string="Hello Everyone th!s is awe$0me 0n3 @@@mm3333"
upper,digit,lower,special=0,0,0,0
for i in string:
    if(i.count(' ')):
        continue
    else:
        if (i.isdigit()):
            digit += 1
        elif (i.islower()):
            lower += 1
        elif (i.isupper()):
            upper += 1
        else:
            special += 1


print("The string is: ", string)
print("The total lower case: ", lower)
print("The total upper case: ", upper)
print("The total digits : ", digit)
print("The total special symbols: ", special)

print("-------------------------------------------------------")

#Write a program to display the n terms of harmonic series and their sum.

num=int(input("Input the number of terms: "))
result=0
for i in range(1,num+1):
    if(i<num):
        print(f"1/{i}", end=" + ")
        result+=1/i

    if(i==num):
        print(f"1/{i}")
        result += 1 / i

print("The sum of series upto {} terms: {}".format(num,round(result,4)))

print("-------------------------------------------------------")

#Print a pattern

row=int(input("Enter the rows for the pattern: "))
k=2*row-2
for i in range(0,row):
    for j in range(0,k):
        print(end=" ")
    k=k-2
    for j in range(0, i+1):
        print("*",end=" ")
    print("")

print("-------------------------------------------------------")

#Create a dictionary that has a key value pair of letters and the number of occurrences of
#that letter in a string.

string=input("Enter a string: ")
sample_dic={}
for i in string:
    if i in sample_dic.keys():
       sample_dic[i]+=1
    else:
        sample_dic[i]=1

print(sample_dic)
