import zipfile as zf

zf = zf.ZipFile('hello.zip',mode='w')

try:
    zf.write('harry.txt')
    zf.write('mike.txt')
finally:
    zf.close()

print('zip file is ready')


