from hashlib import sha1

#文件内容
fileContent = '123\n'
#文件内容长度
fileContentLength = len(fileContent)
#blob文件内容
data = 'blob ' + str(fileContentLength) + "\0" + fileContent
#SHA-1运算
hashObj = sha1()
hashObj.update(data.encode('utf-8'))
hashValue = hashObj.hexdigest()
print(hashValue)
