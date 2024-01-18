# Celsius to Fahrenheit
# The formula to convert a temperature from Celsius to Fahrenheit is:

# F = (C * 9/5) + 32

# Write a function that takes a temperature in Celsius, converts it Fahrenheit,
#  and returns the value.

# def conversion (temp):
#     temp = input("Please provide a temp: ")
#     ctemp = float(temp)
#     ftemp = (ctemp * 9/5) + 32
#     result =  str(ftemp) + " F"
    
#     print(result(temp))
#     return


def conversionCF():
    temp = input("Please provide a Celcius degree to convert to Fahrenheit: ")
    ctemp = float(temp)
    ftemp = (ctemp * 9/5) + 32
    result = str(ftemp) + " F"
    return result  

converted_temp = conversionCF()
print(converted_temp)

def conversionFC():
    temp = input("Please provide a Fahrenheit degree to convert to Celcius: ")
    ftemp = float(temp)
    ctemp = (ftemp - 32) * 5/9
    result = str(ctemp) + " C"
    return result
converted_ftemp = conversionFC()
print(converted_ftemp)
