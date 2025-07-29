#Write a program that converts numbers to word
#Develop an input phase of the number to be converted
#When the number has been entered, convert it to word,
#Note: not just the number that you have automated to be provided but also other numbers as well
#And I think one thing that we should note is that, python might be able to recognize these words and then convert them,
#So there's no box to think outside, just code
phone = input("Phone: ")
digit_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
Output = ""
for ch in phone:
    Output += digit_mapping.get(ch, "!") + " "
print(Output)