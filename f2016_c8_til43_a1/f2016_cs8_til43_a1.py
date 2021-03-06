# name: Tiantian Liu
# email: til43@pitt.edu
# date: Sept. 30. 2016
#class: CS0008-f2016
#instructor: Max Novelli (man8@pitt.edu)

#Description: assignment 1: A client wish to have a software to provide a better understand
#of gas mileage for her car dealer business. Given that she has a lot of international clients,
#she wishes to hace a software that provides results in USC (US Customary Units) and Metric System.

#ask users for the system they use
a = input("If you are using USC, type '1'; If metric, type '2': ")

#ask users for distance and gas input in USC unit, if the user chose USC
if a == 1:
    distance = float(input("How many miles have you driven: "))
    gas = float(input("How many gallons of gasoline was used: "))

    #convert USC to Metric system
    disM = distance * 0.621371
    gasM = gas * 3.78541


#ask users for distance and gas input in Metric unit, if Metric is chose
if a == 2:
    disM = input("How many kilometers have you driven: ")
    gasM = input("How many liters of gasoline was used: ")

#convert Metric to USC
    distance = disM * 1.60934
    gas = gasM * 3.78541

#calculate the fuel consumption
    fuelcomM = 100 * gasM / disM
    fuelcomU = distance / gas

#provide rating for the users
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

#format the numbers
distance_ = format(distance, '.3f')
disM_ = format(disM, '.3f')
gas_ = format(gas, '.3f')
gasM_ = format(gasM, '.3f')
fuelcomU_ = format(fuelcomU, '.3f')
fuelcomM_ = format(fuelcomM, '.3f')

#print the result
print("                            USC                       Metric")
print("Distance___________:" + distance_ + " miles"+"       "+ disM_ +"miles")
print("Gas________________:" + gas_ + " miles"+"       "+ gasM_ +"miles")
print("Consumption________:" + fuelcomU_ + " miles"+"       "+ fuelcomM_ +"miles")
print("Gas Consumption Rating: " + rate )
