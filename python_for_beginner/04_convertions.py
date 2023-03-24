from datetime import date

#If we obtain the current date with the today() method and we want to concatenate it with a string of characters this will show us an error, since the string is a string while the type of data returned by the today method is of type datetime.

# to convert the datetime to a string type we use the function str()
print("Today's date is: "+ str(date.today()))


number_string = '23'  # is string, we have to convert it to integer
number_string_2 = 7   # is the type number

print(number_string_2 + int(number_string))
