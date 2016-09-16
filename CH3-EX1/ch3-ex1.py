# name: Tiantian Liu
# email: til43@pitt.edu
# date: Sept. 16. 2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
#
# Description:
# Chapter3, Exercise 1


a = int(input("Please input a number between 1~7:"))
if a < 1 or a> 7:
    print "Please give me a number within the range :)"

elif a == 1:
    b = "Monday"
elif a == 2:
    b = "Tuesday"
elif a == 3:
    b = "Wednesday"
elif a == 4:
    b = "Thursday"
elif a == 5:
    b = "Friday"
elif a == 6:
    b = "Saturday"
else:
    b = "Sunday"

print b


