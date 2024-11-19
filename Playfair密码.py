# 字母列表中去除'J'
Letter_list = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
#对密钥进行加工处理:去除空格，把J改成I重夏字母
def create_duplicates(key):
    # 密钥转大写
    key = key.upper()
    # 去除空格
    key = key.replace(' ', '')
    # 加工处理后的密钥
    _key = ''
    for ch in key:
        if ch == 'J':
            ch = 'I'
        if ch not in _key:
            _key += ch
    return _key
# 密钥矩阵
def create_matrix(key):
    key = create_duplicates(key)
    remaining_letters = [ch for ch in Letter_list if ch not in key]
    key += ''.join(remaining_letters)  # 添加剩余的字母

    # 确保密钥长度为25
    if len(key) > 25:
        key = key[:25]

    keys = [[key[i + j * 5] for j in range(5)] for i in range(5)]
    return keys
# 蔡取明文字母在密钥矩阵中的位置
def get_matrix_index(ch,keys):
    for i in range(5):
        for j in range(5):
            if ch == keys[i][j]:
                # 返回字符在密钥矩阵中所在的行号和列号
                return i,j
def get_ctext(ch1,ch2,keys):
    # 获取密钥矩阵中字符1和字符2的位置
    index1 = get_matrix_index(ch1,keys)
    index2 = get_matrix_index(ch2,keys)
    # 获取字符1和字符2的行和列
    r1,c1,r2,c2 = index1[0],index1[1],index2[0],index2[1]
    # 如果字符1和字符2在同一行
    if r1 == r2:
        ch1 = keys[r1][(c1 + 1) % 5]
        ch2 = keys[r2][(c2 + 1) % 5]
    # 如果字符1和字符2在同一列
    elif c1 == c2:
        ch1 = keys[(r1 + 1) % 5][c1]
        ch2 = keys[(r2 + 1) % 5][c2]
    # 如果字符1和字符2不在同一行或同一列
    else:
        ch1 = keys[r1][c2]
        ch2 = keys[r2][c1]
    text = ''
    text += ch1
    text += ch2
    return text
def get_ptext(ch1,ch2,keys):
    # 获取密钥矩阵中字符1和字符2的位置
    index1 = get_matrix_index(ch1,keys)
    index2 = get_matrix_index(ch2,keys)
    # 获取字符1和字符2的行和列
    r1,c1,r2,c2 = index1[0],index1[1],index2[0],index2[1]
    # 如果字符1和字符2在同一行
    if r1 == r2:
        ch1 = keys[r1][(c1 - 1) % 5]
        ch2 = keys[r2][(c2 - 1) % 5]
    # 如果字符1和字符2在同一列
    elif c1 == c2:
        ch1 = keys[(r1 - 1) % 5][c1]
        ch2 = keys[(r2 - 1) % 5][c2]
    # 如果字符1和字符2不在同一行或同一列
    else:
        ch1 = keys[r1][c2]
        ch2 = keys[r2][c1]
    text = ''
    text += ch1
    text += ch2
    return text
def playfair_encode(plaintext,key):
    plaintext = plaintext.replace(" ","")
    plaintext = plaintext.upper()
    plaintext = plaintext.replace("J","I")
    plaintext = list(plaintext)
    plaintext.append('#')
    plaintext.append('#')

    keys = create_matrix(key)
    cipertext = ''
    i = 0
    while plaintext[i] != '#':
        if plaintext[i] == plaintext[i + 1]:
            plaintext.insert(i + 1,'X')
        if plaintext[i + 1] == '#':
            plaintext[i + 1] = 'X'
        cipertext += get_ctext(plaintext[i],plaintext[i + 1],keys)
        i += 2
    return cipertext
def playfair_decode(cipertext,key):
    keys = create_matrix(key)
    i = 0
    plaintext = ''
    while i < len(cipertext):
        plaintext += get_ptext(cipertext[i],cipertext[i + 1],keys)
        i += 2
    _plaintext = ''
    _plaintext += plaintext[0]
    for i in range(1,len(plaintext)-1):
        if plaintext[i] != 'X':
            _plaintext += plaintext[i]
        elif plaintext[i] == 'X':
            if plaintext[i - 1] != plaintext[i + 1]:
                _plaintext += plaintext[i]
                _plaintext += plaintext[-1]
    _plaintext = _plaintext.lower()
    return _plaintext

if __name__ == '__main__':
    print('仅限英文字母加解密')
    p = input('请输入明文：')
    key = input('请输入密钥：')
    c = playfair_encode(p,key)
    print('明文为：',p)
    print('密文为：',c)
    p1 = playfair_decode(c,key)
    print('解密后明文为：',p1)

# if __name__ == '__main__':
#     p = 'Above us only sky'
#     key = 'lucky'
#     c = playfair_encode(p, key)
#     print('明文为：', p)
#     print('密文为：', c)
#     p1 = playfair_decode(c, key)
#     print('解密后明文为：', p1)