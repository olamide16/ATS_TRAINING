# def square(num):
#     return num * num
# print(square(76))
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":|"
    }
    output = " "
    for word in words:
        output+= emojis.ger(word, word) + " "
    return output
message = input(">")
print(emoji_converter(message))