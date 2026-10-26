# Problem 2:
# purple : Function 
# blue : Variable
# orange : Object
total_seconds = 86399
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print("====================================")
print(hours,"hours", minutes,"minutes","and", seconds,"seconds")

# check return Value of the Time (==) check True or False

(hours * 3600) + (minutes * 60) + seconds == total_seconds

print("Check the result:", (hours * 3600) + (minutes * 60) + seconds == total_seconds)

# Test your code with 3600, 59 and 86399 seconds.

# print the results with: 3600, 59 the program Error
# print the results with: 86399 the program output: 23 hours 59 minutes and 59 seconds
