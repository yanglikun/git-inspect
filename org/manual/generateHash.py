from hashlib import sha1

fileContent = '789\n'
fileContentLength = len(fileContent)
data = 'blob ' + str(fileContentLength) + "\0" + fileContent

hashObj = sha1()

hashObj.update(data.encode('utf-8'))

hashValue = hashObj.hexdigest()

print(hashValue)
