# 根据加密密钥生成,获取加密置换与解密置换规则的密钥列表
def key_list(key):
    key = list(key)
    keys = [ord(item) for item in key]
    # 找出keys中asccii值最小的字符
    min_key = keys[0]
    for ch in keys:
        if ch < min_key:
            min_key = ch

    keys = [(num - min_key) for num in keys]

    # 创建一个空的列置换密钥列表,len(key)行,2列
    keylist = [[i for j in range(2)] for i in range(len(key))]

    for i in range(len(keys)):
        keylist[i][1] = keys[i]
    return keylist

# 根据明文或密文字符串和密钥生成字符矩阵
def create_matrix(str,key,sel):
    # 矩阵列数
    m = len(key)
    # 矩阵行数
    n = int(len(str) / m)

    # 创建一个空的字符矩阵
    ch_matrix = [[i for j in range(m)] for i in range(n)]

    # sel 0:加密 1:解密
    if sel == 0:
        for i in range(len(str)):
            ch_matrix[i // n][i % n] = str[i]
    elif sel == 1:
        index = 0
        for j in range(m):
            for i in range(n):
                ch_matrix[i][j] = str[index]
                index += 1
    return ch_matrix

# 列置换函数
def swit_col(chs,key,sel):
    # 生成密钥列表
    keylist = key_list(key)
    # 生成字符矩阵
    ch_matrix = create_matrix(chs,key,sel)

    # 矩阵列数
    m = len(key)
    # 矩阵行数
    n = int(len(chs) / m)

    ch1 = []
    for i in range(m):
        chs_temp = ''
        for j in range(n):
            chs_temp += ch_matrix[j][i]
        ch1.append(chs_temp)
    ch2 = []
    for i in range(m):
        for j in range(m):
            if keylist[j][1] == i:
                ch2.append(ch1[j])
    ch2 = ''.join(ch2)
    index = 0
    for i in range(m):
        for j in range(n):
            ch_matrix[j][i] = ch2[index]
            index += 1
    # 0:加密 1:解密
    if sel == 0:
        return ch2
    elif sel == 1:
        ch2_ = ''
        for i in range(n):
            for j in range(m):
                ch2_ += ch_matrix[i][j]
        return ch2_

def enCode(p,key):
    # 加密模式
    sel = 0
    c = swit_col(p,key,sel)
    return c
def dnCode(c,key):
    # 解密模式
    sel = 1
    p = swit_col(c,key,sel)
    return p

if __name__ == '__main__':
    p = 'The XXIV Olympic Winter Games'
    p = p.replace(' ','')

    key_c = '45132'
    key_p = '35412'

    # n行m列矩阵
    m = len(key_c)
    if len(p) % m != 0:
        a = m - int(len(p) % m)
        print(f'明文字符串还需要输入{a}个字母！！')
    else:
        c = enCode(p,key_c)
        print('密文:',c)
        p = dnCode(c,key_p)
        print('明文:',p)