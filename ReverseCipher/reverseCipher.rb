=begin
    待补充功能：1. 从命令行读取文本文件 2. 从命令行读取一个字符串列表
=end

rawString = "I Love You!"
# 第一个参数为字符串
unless ARGV[0] == nil then
    rawString = ARGV[0]
else
    # 无命令行参数，可输入字符串
    puts "请输入要反向加密的语句："
    print "请输入："
    rawString = gets.chomp
end

def reverseCipher(rawString)
    strLength = rawString.size
    reversedString = ''
    while strLength > 0
        reversedString += rawString[strLength - 1]
        strLength -= 1
    end
    return reversedString
end

reversedString = reverseCipher(rawString)

puts "反向加密结果为："
puts reversedString
