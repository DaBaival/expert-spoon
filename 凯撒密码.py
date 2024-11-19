# 定义一个加密函数
def Ecrytion():
    # 获取用户输入的字符串
    c= input('请输入需要加密的字母：')
    # 定义一个空字符串用于存放加密后的字符
    p = ''
    # 遍历字符串中的每一个字符
    for i in c:
        # 判断字符是否为小写字母
        if 'a' <= i <= 'z':
            # 计算加密后的字符的ASCII码
            p += chr((ord(i) - 97 + 3) % 26 + 97)
        # 判断字符是否为大写字母
        elif 'A' <= i <= 'Z':
            # 计算加密后的字符的ASCII码
            p += chr((ord(i) - 65 + 3) % 26 + 65)
        # 如果不是字母，直接添加到结果字符串中
        else:
            p += i
    # 输出加密后的字符串
    print(p)

# 定义一个解密函数
def Deciphering():
    # 获取用户输入的字符串
    c= input('请输入需要解密的字姆')
    # 定义一个空字符串用于存放解密后的字符
    p = ''
    # 遍历字符串中的每一个字符
    for i in c:
        # 判断字符是否为小写字母
        if 'a' <= i <= 'z':
            # 计算解密后的字符的ASCII码
            p += chr((ord(i) - 97 - 3) % 26 + 97)
        # 判断字符是否为大写字母
        elif 'A' <= i <= 'Z':
            # 计算解密后的字符的ASCII码
            p += chr((ord(i) - 65 - 3) % 26 + 65)
        # 如果不是字母，直接添加到结果字符串中
        else:
            p += i
    # 输出解密后的字符串
    print(p)

# 定义一个主程序函数,选择加解密模式
def main():
    # 提示用户输入
    print('仅限英文字母加解密')
    # 定义一个选择模式的变量
    sel = int(input('请选择加密模式或者解密模式(0:加密,1:解密)'))
    # 判断模式
    if sel == 0:
        # 调用加密函数
        Ecrytion()
    elif sel == 1:
        # 调用解密函数
        Deciphering()
    else:
        # 提示用户选择正确的模式
        print('请选择正确的模式')

# 判断是否为主程序
if __name__ == '__main__':
    # 调用主程序函数
    main()