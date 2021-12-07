rawString = "I Love You!"

print("请输入要反向加密的语句：")
rawString = input("请输入：")

def reverseCipher(rawString):
    strLength = len(rawString)
    reversedString = ''
    while strLength > 0:
        reversedString += rawString[strLength - 1]
        # print(reversedString)
        strLength -= 1
    
    return reversedString

print("反向加密结果为：")
print(reverseCipher(rawString))