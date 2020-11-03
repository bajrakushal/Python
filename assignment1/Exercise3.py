#Write a program that takes seconds as time units and converts it to minutes and seconds.
time=int(input("Enter your time in seconds: "))
minutes=time // 60
seconds=time%60
print(time ,"seconds results in ",minutes, "minutes and ",seconds," seconds")
