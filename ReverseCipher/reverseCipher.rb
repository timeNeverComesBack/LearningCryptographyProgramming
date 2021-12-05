rawString = "I Love You!"

puts "请输入要反向加密的语句："
print "请输入："
rawString = gets.chomp

def reverseCipher(rawString)
    strLength = rawString.size
    reversedString = ''
    while strLength > 0
        reversedString += rawString[strLength - 1]
        strLength -= 1
    end
    return reversedString
end

puts "反向加密结果为："
puts reverseCipher(rawString)
