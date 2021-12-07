# chr()
# ord()
# 待加密字符串
rawString = "AWP"
# 密钥
key = 13
# 字符字典(多种字典)
SYMBOLS_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?,."
SYMBOLS_2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 !?,."
SYMBOLS_3 = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !?,."
SYMBOLS_4 = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !?,."
SYMBOLS_5 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890 !?,."
SYMBOLS_6 = "aAbBcCdDeEfFgGhHiIjJkklLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890 !?,."
# 字符字典列表
SYMBOLS = [SYMBOLS_1, SYMBOLS_2, SYMBOLS_3, SYMBOLS_4, SYMBOLS_5, SYMBOLS_6]

rawString = input("请输入字符串：")
print("请选择字典（用于加解密）：")
for ss in SYMBOLS:
    print("加密字典" + str(SYMBOLS.index(ss) + 1) + "： " + ss)
symbolNumber = int(input("选择序号：")) - 1

key = int(input("设置密钥（0~25内的整数）："))
print("请选择：加密 0，解密 1 ：")
cryptType = int(input("0 or 1:"))

def caesarCipher(rawString, key = 13, symbolNumber = 0, cryptType = 0):
    if cryptType == 0:
        # 调用加密函数
        print("正在加密……")
        return CaesarEncrypt(rawString, key, symbolNumber)
    else:
        # 调用解密函数
        print("正在解密……")
        return CaesarDecrypt(rawString, key, symbolNumber)

def CaesarEncrypt(rawString, key, symbolNumber):
    symbols = SYMBOLS[symbolNumber]
    caesarString = ''
    for character in rawString:
        if character in symbols:
            charIndex = symbols.find(character)
            charIndex += key
            # 回环操作 P1
            charIndex = charIndex % len(symbols)
            # 回环操作 P2
            # if charIndex >= len(symbols):
            #     print(charIndex)
            #     charIndex -= len(symbols)
            # elif charIndex < 0:
            #     print(charIndex)
            #     charIndex += len(symbols)

            caesarString += symbols[charIndex]
        else:
            caesarString += character

    return caesarString

def CaesarDecrypt(rawString, key, symbolNumber):
    symbols = SYMBOLS[symbolNumber]
    caesarString = ''
    for character in rawString:
        if character in symbols:
            charIndex = symbols.find(character)
            charIndex -= key
            charIndex = charIndex % len(symbols)
            caesarString += symbols[charIndex]
        else:
            caesarString += character
    return caesarString

print(caesarCipher(rawString, key, symbolNumber, cryptType))