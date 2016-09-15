#name: Tiantian Liu
#email: til43@pitt.edu
#date: Sept. 15. 2016
#class: CS0008-f2016
#instructor: Max Novelli (man8@pitt.edu)
#Description:
#Chapter 3, Exercise 9

a = int(input("input a number from 0~36:"))
if a == 0:
    print "green"
elif a >= 1 and a <= 10:
    if a % 2 == 0:
        print "black"
    else:
        print "red"
elif a >= 11 and a <= 18:
    if a % 2 == 0:
        print "red"
    else:
        print "black"
elif a >= 19 and a <= 28:
    if a % 2 == 0:
        print "black"
    else:
        print "red"
elif a >= 29 and a <= 36:
    if a % 2 == 0:
        print "red"
    else:
        print "black"
else:
    print "wrong"