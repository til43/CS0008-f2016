#name: Tiantian Liu
#email: til43@pitt.edu
#date: Sept. 15. 2016
#class: CS0008-f2016
#instructor: Max Novelli (man8@pitt.edu)
#Description:
#Chapter 3, Exercise 9

a = int(input("input a number from 0~36:"))
if a < 0 or a > 36:
    print "Please give me a number within the range :)"
elif a == 0:
    color = "Green"
elif a >= 1 and a <= 10 \
        or \
                        a >= 19 and a <= 28:
    if a % 2 == 0:
        color = "black"
    else:
        color = "red"
else :
    if a % 2 == 0:
        color = "red"
    else:
        color = "black"
print color



