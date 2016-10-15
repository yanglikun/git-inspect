import zlib

objDir = "E:/git/course/test/.git/objects";
prefixDir = "19"
fileName = "0a18037c64c43e6b11489df4bf0b9eb6d2c9bf"

#读取文件
zlibBinaryData = open(objDir + "/" + prefixDir + "/" + fileName, 'rb').read()

#zlib解压
binaryData = zlib.decompress(zlibBinaryData);

#输出内容
print(binaryData.decode('utf-8'))


