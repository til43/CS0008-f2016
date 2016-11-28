# name: Tiantian Liu
# email: til43@pitt.edu
# date: Oct. 27. 2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)

# Description: A program that loops indefinitely asking the user to enter the name of a text file.
# Then loop on all the lines, counting how many lines you have in each file and providing a running tally on
# how much is the total distance run.
# Then provide the partials for each file and the overall total encompassing all the files.
# The program loops indefinitely until the user enters an empty string, the word "quit" or the letter "q".



total_lines = 0
total_distance = 0.00

# MN: where are the function input arguments?
# define processFile function
def processfile():

    # MN: DO NOT USE global variable unless it is absolutely necessary
    #global variable
    global total_lines
    global total_distance

    # MN: where is file_name defined? which is the variable scope?
    #open the file chosen
    infile = open(file_name, 'r')
    printKV('\nFile to be read:', file_name)

    #initialize the values
    partial_sum_distance = 0.00
    partial_sum_lines = 0

    #use for loop to get the partial sum of lines and distances run in each file
    for line in infile:
        run_distance = float(line.split(',')[1].rstrip('\n'))
        partial_sum_lines += 1
        partial_sum_distance += run_distance

        #close the file
    infile.close()
    printKV('Partial Total # of lines:', partial_sum_lines, 25)
    printKV('Partial distance run:',partial_sum_distance, 25)

    # MN: these statements should not be in this function but in the main loop
    #get the total number of lines
    total_lines += partial_sum_lines
    total_distance += partial_sum_distance

    #return partial value
    return partial_sum_lines, partial_sum_distance


# define printKV
def printKV(key, value, klen=0):
    formkey = '{:<25}'. format(key)
    formvalue = 0

    #test the type of value and assign format accordingly.
    if isinstance(file_name, str):
        formvalue = '{:<20}'.format(value)
    elif isinstance(value,float):
        formvalue = '{:<10.3f}'.format(value)
    elif isinstance(value, int):
        formvalue = '{:<10}'.format(value)

    print(formkey, ':', formvalue)

    return

#ask users for the file names
file_name = input("enter valid file name choose file, enter 'quit' if you finish: ")

# MN: this loop is not an infinite loop
# MN: what happens if I provide a file with a different name?
#     lines and distances do not get counted
# MN: I would use the following loop
#loops indefinitely
#while file_name == 'f2016_cs8_a2.data.1.csv' or file_name == 'f2016_cs8_a2.data.2.csv':
while file_name and file_name != "q" and file_name != "quit":
    # MN: what if I provide in input a file that is named "test.csv" and is a valid file?
    #     I would not use this conditional statement testing on the file names
    #     but just on the exit values aka sentinels
    #if file_name =='f2016_cs8_a2.data.1.csv':
    #    processfile()
    #else:
    #    file_name = 'f2016_cs8_a2.data.2.csv'
    #    processfile()

    # MN: process the file
    processfile()
    # MN: ask for the next file
    file_name = input("enter '1'or '2'to choose file, enter 'quit' if you finish: ")

#if the user choose quit, compute the total result
else:
    printKV('file to be read: ', file_name)
    print('\nTotals')
    printKV('Total # of lines:', total_lines, 25)
    printKV('Total distance run:', total_distance, 25)













