__author__ = 'yanglikun'
import struct


def readStr(file, byteNum):
    return file.read(byteNum).decode('utf-8')


def readnum(file, byteNum):
    return struct.unpack(">i", file.read(byteNum))[0]


def skip(file, byteNum):
    file.read(byteNum)


file = open(r'E:\git\test\tmp\.git\index', 'rb')

# 签名DIRC代表了(stands for "dircache")
signatureData = readStr(file, 4)
print(signatureData)

# 当前的版本，支持的有2,3,4
versionData = readnum(file, 4)
print(versionData)

# 暂存区实体的数量
entriesNum = readnum(file, 4)
print(entriesNum)

# 32位(4 byte)扩展信息
# 扩展属性的第一个字符
extensionFirstChar = readStr(file, 1)
print(extensionFirstChar)
skip(file, 3)

skip(file, 4)


# 160 bit (20 byte)
# contentSHA=readStr(file,20)
# print(contentSHA)
# skip(file,20)
#
# # 32 bit(4 byte) 时间:文件元信息修改的时间
# ctime = readnum(file, 4)
# print(ctime)
#
# #各种时间、文件大小信息 32*10/8 byte
# skip(file,40)
#
# #sha-1 160bit(20byte)
# sha=readStr(file,20)
# print(sha)
