import base64
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
from Crypto.PublicKey import RSA

def create_rsa_pair():
    '''
    创建rsa公私钥对
    :return public_key,private_key:
    '''
    # 生成一个1024位的RSA密钥对的
    f = RSA.generate(1024)
    private_key = f.exportKey('PEM') # 生成私钥
    public_key = f.publickey().exportKey() # 生成公钥
    return public_key,private_key
def encryption(text:str,public_key:bytes):
    # 字符串指定编码(转为bytes)
    text = text.encode('utf-8')
    # 构建公钥对象
    cipher_public = PKCS1_v1_5.new(RSA.importKey(public_key))
    # 加密(bytes)
    text_encrypted = cipher_public.encrypt(text)
    # base64编码,并转为字符串
    text_encrypted_base64 = base64.b64encode(text_encrypted).decode()
    return text_encrypted_base64

def decryption(text_encrypted_base64:str,private_key:bytes):
    # 字符串指定编码 (转为 bytes)
    text_encrypted_base64 = text_encrypted_base64.encode()
    # base64解码
    text_encrypted = base64.b64decode(text_encrypted_base64)
    # 构建私钥对象
    cipher_private = PKCS1_v1_5.new(RSA.importKey(private_key))
    # 解密(bytes)
    text_decrypted = cipher_private.decrypt(text_encrypted,Random.new().read)
    # 解码为字符串
    text_decrypted = text_decrypted.decode()

    return text_decrypted

if __name__ == '__main__':
    # 生成密钥对
    public_key,private_key = create_rsa_pair()
    # 加密
    text = '123456'
    text_encrypted_base64 = encryption(text,public_key)
    print('密文:',text_encrypted_base64)
    # 解密
    text_decrypted = decryption(text_encrypted_base64,private_key)
    print('明文:',text_decrypted)