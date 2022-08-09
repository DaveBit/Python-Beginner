def emoji_converter(message):
    words = message.split(' ') #takes de message and splits it by spaces into an array. 
    # [hola, hoy, estoy, contento]
    emojis = {
    ":)" : "😀",
    ":(" : "😢"
    }
    output = ""
    for word in words: 
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))

