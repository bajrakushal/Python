"""
    Implement question number 1, 2 and 4 from Session 2 Exercise as different functions in a single
    Exercise 1: Choose a list of your choice and find the sum of all elements of that list.
    Exercise 2: Write a program that returns a list which contains common elements from two lists. Avoid
    the duplicate elements from lists.
    Exercise 4: Write a code to ask an input from the user which is a string and display the string along
    with its length.
"""
def list_sum(items):
    sum=0
    for i in items:
        sum+=i
    return  sum

def common_list(list1, list2):
    set_a=set(list1)
    set_b=set(list2)
    return set_a.intersection(set_b)

def len_string(value):
    count=0
    for i in value:
        count+=1
    return count


def main():
    list1=[20,5,6,8,10,22,33,0,45]
    print("The sum of the list {} is {}".format(list1,list_sum(list1)))
    print("-----------------------------------")
    list2=[1,2,5,8,10,15,20]
    print("The common items in the list of {} and {}".format(list1,list2))
    print("Common: ",list(common_list(list1,list2)))
    print("-----------------------------------")
    string=input("Enter a string: ")
    print("The length of the string {} is {}".format(string,len_string(string)))


if __name__ == '__main__':
    main()