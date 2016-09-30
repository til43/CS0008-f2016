#name: Tiantian Liu
#email: til43@pitt.edu
#date: Sept. 30. 2016
#class: CS0008-f2016
#instructor: Max Novelli (man8@pitt.edu)
#
#Description: assignment 1: A client wish to have a software to provide a better understand
#of gas mileage for her car dealer business. Given that she has a lot of international clients,
#she wishes to hace a software that provides results in USC (US Customary Units) and Metric System.

#ask users for the system they use
a = input("If you are using USC, type 'USC'; If metric, type 'Metric': ")

#ask users for distance and gas input in USC unit, if the user chose USC
if a == "USC":
    distance = float(input("How many miles have you driven: "))
    gas = float(input("How many gallons of gasoline was used: "))

    #convert USC to Metric system
    disM = distance * 0.621371
    gasM = gas * 3.78541

    #calculate the fuel consumption
    fuelcomU = distance / gas
    fuelcomM = 100 * gasM /disM

    #provide rating for the users
    if fuelcomM > 20:
        rate = "Extremely poor"
    elif fuelcomM > 15 and fuelcomM <= 20:
        rate = "Poor"
    elif fuelcomM > 10 and fuelcomM <= 15:
        rate = "Average"
    elif fuelcomM > 8 and fuelcomM <=10:
        rate = "Good"
    else:
        rate = "Excellent"

#ask users for distance and gas input in Metric unit, if Metric is chose
if a == "Metric":
    disM = float(input("How many kilometers have you driven: "))
    gasM = float(input("How many liters of gasoline was used: "))

    #convert Metric to USC
    distance = disM * 1.60934
    gas = gasM * 3.78541

    #calculate the fuel consumption
    fuelcomM = 100 * gasM / disM
    fuelcomU = distance / gas

    # provide rating for the users
    if fuelcomM > 20:
        rate = "Extremely poor"
    elif fuelcomM > 15 and fuelcomM <= 20:
        rate = "Poor"
    elif fuelcomM > 10 and fuelcomM <= 15:
        rate = "Average"
    elif fuelcomM > 8 and fuelcomM <= 10:
        rate = "Good"
    else:
        rate = "Excellent"

print "                             USC                         Metric"
print "distance                    ", distance, "miles","       ", disM,"Km"
