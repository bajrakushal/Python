"""
    Implement question number 1, 2 and 6 from Session 3 Exercise as different functions
    Exercise 1: Write a program to display all prime numbers from 1 to 100.
    Exercise 2: Ask the user for a string and print out whether this string is a palindrome or not.
    Exercise 6: Create a dictionary that has a key value pair of letters and the number of occurrences of
    that letter in a string.

"""
def prime_numbers(num):
    if num==1 or num==2:
        return True
    else:
        for i in range(2,num//2+1):
            if(num%i ==0):
                return False
        else:
            return True


def is_palindrome(value):
    revere=""
    for i in range(len(value)-1,-1,-1):
        revere+=value[i]

    if(value==revere):
        return True
    else:
        return False

def dic_sample(value):
    sample_dic={}
    for i in value:
        if i in sample_dic.keys():
            sample_dic[i]+=1
        else:
            sample_dic[i]=1

    return sample_dic



def main():
    for i in range(1,101):
        if(prime_numbers(i)):
            print(i, end=" ")
    print("\n----------------------------------------")

    string=input("Enter a string: ")
    if(is_palindrome(string)):
        print("The string is palindrome.")
    else:
        print("The string is not palindrome.")
    print("\n----------------------------------------")
    print(dic_sample(string))


if __name__ == '__main__':
    main()