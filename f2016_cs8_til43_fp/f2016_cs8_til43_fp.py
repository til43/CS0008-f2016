#
#
# name       : Tiantian Liu
# email      : man8@pitt.edu
# date       : 2016/12/09
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# description:
# A customer needs to process a number of text files (called data files) that contain names and distance run by study participants.
# The format of those files is as follows:
#
# Max ,34.23
# Barbara ,23.00
# Luka ,12.87
# …
#
# In those files, each row is a comma separated list of 2 values: the first one is the name of the participant and the
# second is the distance that the participant has run.
# The names of the input files are stored one per line in an additional file, called the master input list.
# This file has the following structure:
#
# <data file 1>
# <data file 2>
# <data file 3>
# …
#
# Write a program that read the master input list file, retrieves the names of the data files and from each one of them
# reads every line, extract name and distance. Once the program has all the data in memory, it has to compute the following
# quantities and informations:
# - number of files read in input
# - total number of lines read
# - total distance run (aka the sum of all the distances loaded from provided files)
# - total distance run for each individual participant
# - individual maximum distance run and by which participant
# - individual minimum distance run and by which participant
# - report if there are any participants that appears more than once, how many times and their names
# - total number of participants
#
# The program should provide an terminal output similar to the following:
#
#	Number of Input files read   : xx
#	Total number of lines read   : xx
#
#	total distance run           : xxxx.xxxxx
#
#	max distance run             : xxxx.xxxxx
#	  by participant             : participant name
#
#	min distance run             : xxxx.xxxxx
#	  by participant             : participant name
#
# in this program, students should make the best use of everything that has learn so far in this class, she
# or he has to use a class named participants that has 2 properties:
# name; distance; runs;
# and at least, the following methods:
# addDistance(d): add single distance to the distance accumulator and increments runs by 1, argumentd is
#                   a single float.
# addDistances(ld): add an array of distances to distance accumulator. Argument ld is a list of floats.
# getDistance(): get the current value of the distance accumulator
# getName(): get the name of the participant of the current instance
# __init__(n,d=0): initializer method. Set name and initial distance if provided. if initial distance is not
#                   specified, it should be set to 0
# __str__(): stringify method. Returns a string with name, total distance run and how many distances the
#               object added, according to the following format:
# Name : xxxxxxxxxxxxxxxxxxx. Distance run : yyyy.yyyy. Runs : zzzz
# where xxxxxxxxxxxxxxxxxxx is a right align string of 20 characters for the name, yyyy.yyyy is the total
# distance tun with 9 digits, decima point and 4 decimals, and zzzz is the number of runs with 4 digits,
# no decimals.

# start the program with the class
class Participant:
    # initialize the properties
    def __init__(self,name,distance=0):
#       #set name
        self.name = 'name'
#       set distance and runs
        if distance > 0:
            self.distance = distance
            runs = 1
        else:
            self.distance = 0
            runs = 0
    # def __init__ ends
#
    # addDistance(d) method
    def addDistance(self,distance):
        if distance > 0:
            self.distance = distance
            self.runs +=1
    # end def addDistance

    # addDistances(ld) method
    def addDistances(self,distances):
        for distance in distances:
            if distance > 0:
                self.distance += distance
                self.runs += 1
    # end def addDistances

    # getDistance method
    def getDistance(self):
        return self.distance
    # end def getDistance

    # getName
    def getName(self):
        return self.name
    # end def gerName

    # __str__method
    def __str__(self):
        return \
            "Name : " + format(self.name, '>20s') + \
            ". Distance run : " + format(self.distance, '9.4f') + \
            ". Runs : " + format(self.runs, '4d')

    # write into a csv file method
    def incsv(self):
        return ",". join([str(self.name),str(self.distance), str(self.runs)])
    # end def inscv


# printKV function
def printKV(key,value,klen = 0):
    # max of klen and the length of key
    klen = max(klen,len(key));
    # assign different format to different type of value
    if isinstance(value,str):
        # string
        fvalue = '20s'
    elif isinstance(value,float):
        # float
        fvalue = '9.4f'
    elif isinstance(value,int):
        # integer
        fvalue = '4d'
    else:
        value = str(value)
        fvalue = '20s'

    # print key and value with correct formatting
    print(format(key,'>'+str(klen)+'s'),' : ',format(value,fvalue))



# put files to be read in a file list
masterFile = open('f2016_cs8_fp.data.txt', 'r')
fileList = []
# initiate the total distances
totalDistance = 0
# create an empty list
data=[]
# initiate the total number of files read
totalnumFile = 0
# loop and read filenames to a list
for filename in masterFile:
    totalnumFile += 1
    fileList.append(filename.rstrip('\n'))

# loop through all three files and append all data to data list
for file in fileList:
    files = open(file, 'r')
    # append all datas to the data list
    for line in files:
        data.append(line.rstrip('\n').split(','))
    # end for
# end for

# the number of total lines read
totalLines = len(data)
# total distances run

# get the total distance
for items in data:
    if items[1] != 'distance':
        totalDistance += float(items[1])
# end for

# create a dictionary
participant = {}

# loop through all the datas and build the dictionary
for item in data:
    # exclude 'name' and 'distance' in the dictionary
    if item[0] != 'name' and item[1] != 'distance':
        participant.update({str(item[0]): float(item[1])})
        distance = float(item[1])
        name = item[0]
        if name in participant.keys():
           name.addDistance(item[1])$

# total number of participants
totalParticipants = len(participant)









