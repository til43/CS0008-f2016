# name: Tiantian Liu
# email: til43@pitt.edu
# date: Sept. 12. 2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# Description:
# Chapter2, Exercise 10

cookies = input("Number of cookies you want to make: ")
sugar = 300 * (cookies/48.0)
butters = 240 * (cookies/48.0)
flour = 330 * (cookies/48.0)
print "To make", cookies, "cookies,", "you need:", sugar, "gr of sugar;",\
    butters, "gr of butters;", flour, "gr of flours."
