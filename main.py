import os
import shutil
for root, dirs, files in os.walk(r'E:\zakaz'):
    for file in files:
        if file.endswith('Tokens.txt'):
            a = (root, file)
            file1 = open(os.path.join(root, file), 'r')
            textfile1 = file1.read()
            file2 = open('tok.txt', 'a+')
            file2.write(textfile1 + "\n\n")
            file2.read()
            print(textfile1)
            file1.close()
            file2.close()
