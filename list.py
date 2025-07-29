# Write a programme to remove duplicate numbers in a list
# First off create a list with duplicate numbers,
#Identify the duplicate numbers incumbent in the list
#the using the concept of the loop to find the largest number use it to find a repeated occurrence of the number and print out
unique_list = [1,1,2,3,4,5,6,7,7,8,8,9,9]
unique = []
for number in unique_list:
    if number not in unique:
        unique.append(number)
print(unique)
