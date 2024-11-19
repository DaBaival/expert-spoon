letter_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def Get_KeyList(key):
    key_list = []
    for ch in key:
        key_list.append(ord(ch.upper()) - 65)
    return key_list

def Encrypt(message, key):
    key_list = Get_KeyList(key)
    cipher_text = ""
    i = 0
    for ch in message:
        if 0 == i % len(key_list):
            i = 0
        if ch.isalpha():
            if ch.isupper():
                cipher_text += letter_list[(ord(ch) - 65 + key_list[i]) % 26]
            else:
                cipher_text += letter_list[(ord(ch) - 97 + key_list[i]) % 26].lower()
            i += 1
        else:
            cipher_text += ch
    return cipher_text

def Decrypt(cipher_text, key):
    key_list = Get_KeyList(key)
    decrypted_text = ""
    i = 0
    for ch in cipher_text:
        if 0 == i % len(key_list):
            i = 0
        if ch.isalpha():
            if ch.isupper():
                decrypted_text += letter_list[(ord(ch) - 65 - key_list[i] + 26) % 26]
            else:
                decrypted_text += letter_list[(ord(ch) - 97 - key_list[i] + 26) % 26].lower()
            i += 1
        else:
            decrypted_text += ch
    return decrypted_text

def main():
    print('仅限英文字母加解密')
    key = input('请输入密钥: ')
    message = input('请输入要加密/解密的消息: ')
    sel = int(input('请选择加密模式或者解密模式(0:加密,1:解密)'))

    # 判断模式
    if sel == 0:
        # 调用加密函数
        print('加密后的消息:', Encrypt(message, key))
    elif sel == 1:
        # 调用解密函数
        print('解密后的消息:', Decrypt(message, key))
    else:
        # 提示用户选择正确的模式
        print('请选择正确的模式')

if __name__ == '__main__':
    main()