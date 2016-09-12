# name: Tiantian Liu
# email: til43@pitt.edu
# date: Sept. 12. 2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# Description:
# Chapter2, Exercise 7

miles = input("miles driven: ")
kilometers = 1.60934 * float(miles)
gas = input("gas used: ")
Lper100km = 100 * gas / kilometers

print kilometers, "km driven: "
print gas, "liters gas used: "
print "Your car's fuel consumption is ", Lper100km, "liters per 100 Kilometers"


