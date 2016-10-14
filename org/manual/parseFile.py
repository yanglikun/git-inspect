import zlib

objDir = "E:/git/course/test/.git/objects";
prefixDir = "0c"
fileName = "2b7810b5ff9dc14a44270f1f9c3bae28f74855"

zlibBinaryData = open(objDir + "/" + prefixDir + "/" + fileName, 'rb').read()

binaryData = zlib.decompress(zlibBinaryData);

print(binaryData.decode('utf-8'))


