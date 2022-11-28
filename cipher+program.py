def cipherMessage():
    inputText = input("Enter your text to encode:\r\n")
    shiftAmt = int(input("Enter how many places to shift:\r\n"))

    cipherText = ""
    for char in inputText:
        charPosition = ord(char)
        if 48 <= charPosition <= 57:
            newCharPosition = (charPosition - 48 + shiftAmt) % 10 + 48
        elif 65 <= charPosition <= 90:
            newCharPosition = (charPosition - 65 + shiftAmt) % 26 + 65
        elif 97 <= charPosition <= 122:
            newCharPosition = (charPosition - 97 + shiftAmt) % 26 + 97
        else:
            newCharPosition = charPosition
        cipherText += chr(newCharPosition)

    print("Encoded Message (" + str(shiftAmt) + " places): ")
    print(cipherText)

def decipherMessage():
    inputText = input("Enter your text to decode:\r\n")
    shiftAmt = int(input("Enter the secret shift number:\r\n"))

    outputText = ""
    for char in inputText:
        charPosition = ord(char)
        if 48 <= charPosition <= 57:
            newCharPosition = (charPosition - 48 - shiftAmt) % 10 + 48
        elif 65 <= charPosition <= 90:
            newCharPosition = (charPosition - 65 - shiftAmt) % 26 + 65
        elif 97 <= charPosition <= 122:
            newCharPosition = (charPosition - 97 - shiftAmt) % 26 + 97
        else:
            newCharPosition = charPosition
        outputText += chr(newCharPosition)

    print("Decoded Message:")
    print(outputText)

cipherMessage()
decipherMessage()
