def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😒"
    }
    output = ""
    for ch in words:
        output += emojis.get(ch, ch) + " "
    return output


message = input(">")
print(emoji_converter(message))