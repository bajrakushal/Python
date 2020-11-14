"""
    Implement question number 2, 3, 4 and 5 from Session 1
    Exercise as different functions in a single file.
    Exercise 2. Write a program that will convert Fahrenheit to Celsius in degrees.
    Exercise 3. Write a program that takes seconds as time units and converts it to minutes and
    seconds.
    Exercise 4. Consider a list of any arbitrary elements. Your code should print the length of the list
    and first and fourth element of the list.
    Exercise 5. Create a list of any arbitrary elements. Your code should show the list methods as
    pop, insert and remove.
"""
def fahrenheit_celsius(num):
    celcius = (num - 32) * 5 / 9
    return round(celcius,2)

def time_second(time):
    minutes=time // 60
    second= time % 60
    return "{} mintues and {} seconds".format(minutes, second)


def list_numbers(items):
    length=len(items)
    first_number = items[0]
    fourth_number = items[3]
    return "The length of the list is {} and the first and the fourth item is {} and {}".format(length,first_number,fourth_number)

def list_methods(items):
    items.pop(6)
    items.remove(1200)
    items.insert(2,11)
    return items


def main():
    fahernheit = float(input("Enter temperature to convert into Celcius: "))
    print("The celcis degree of ", fahernheit ,"F is ", fahrenheit_celsius(fahernheit) ,"C")
    print("------------------------------------------")
    time = int(input("Enter your time in seconds: "))
    print(time_second(time))
    print("------------------------------------------")
    _list=[15,10,70,32,1200,120,20,50,70,89,63]
    print(list_numbers(_list))
    print("------------------------------------------")
    print(list_methods(_list))
    print("------------------------------------------")



if __name__ == '__main__':
    main()
