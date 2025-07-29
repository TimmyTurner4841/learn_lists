scores = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
max_number = scores[0]
for numbers in scores:
    if numbers > max_number:
        max_number = numbers
print(max_number)