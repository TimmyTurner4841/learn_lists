scores = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
max_number = scores[0]
for numbers in scores:
    if numbers > max_number:
        max_number = numbers
print(max_number)

scores2 = [1,2,3,4,5,6,7,8,9,0,100]
max_number2 = scores2[0]
for number in scores2:
    if number > max_number2:
        max_number2 = number
print(max_number2)

scores3 = [212,1,32,4,4,54,5,65,67,68,7,9,89,0,6,5,4,5,3,4,5,4,56,7,8,99,7,65,4,53,4,5,6,78,9,7,65,43,5,67,89]
max_number3 = scores3[0]
for number2 in scores3:
    if number2 > max_number3:
        max_number3 = number2
print(max_number3)