def symbolsChoose(choice):
    # 字符字典(多种字典)
    SYMBOLS_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?,."
    SYMBOLS_2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 !?,."
    SYMBOLS_3 = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !?,."
    SYMBOLS_4 = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !?,."
    SYMBOLS_5 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890 !?,."
    SYMBOLS_6 = "aAbBcCdDeEfFgGhHiIjJkklLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890 !?,."
    # 字符字典列表
    SYMBOLS = (SYMBOLS_1, SYMBOLS_2, SYMBOLS_3, SYMBOLS_4, SYMBOLS_5, SYMBOLS_6)
    return SYMBOLS[choice]

def bruteCrackCaesar(rawString, symbols):
    caesarArray = []
    for key in range(len(symbols)):
        caesarString = ''
        for character in rawString:
            if character in symbols:
                charIndex = symbols.find(character)
                charIndex -= key
                charIndex = charIndex % len(symbols)
                caesarString += symbols[charIndex]
            else:
                caesarString += character
        caesarArray.append(caesarString)
    return caesarArray

result = bruteCrackCaesar("Tvv", symbolsChoose(0))

print(result)