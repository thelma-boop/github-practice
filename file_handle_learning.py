# -*- coding: utf-8 -*-


folder = "D:\\GIT-Practice\\"

path = folder + "hello_world.md"

photo = folder + "sheep.png"

subfolder = folder + "\\sub"

##-----------------------------------------------------------------

'''
## 相同於下方 第 21~23 行內容
f = open(path)      # OPEN a file------------- MUST

print(f.read())     # READ a file

f.close()           # CLOSE a file------------ MUST
'''


##-----------------------------------------------------------------

'''
## 相同於上方 第 10~14 行內容
with open(path) as f:   # Use "with", you don't need to care about "CLOSE a file"
    print(f.read())
'''
    
##-----------------------------------------------------------------

'''
## 將多行文字 一列一列 印出：【一】
## 有多行文字時，需用多個 readline() 將每一行印出
with open(path) as f:
    print(f.readline())     # READ the 1st line
    print(f.readline())     # READ the 2nd line
'''

'''
## 將多行文字 一列一列 印出：【二】
## 有多行文字時，亦可用 FOR迴圈 將每一行印出
with open(path) as f:
    for l in f:
        print(l)
'''

'''
## 讀取文件裡，N個字元
with open(path) as f:
    print(f.read(5))        # READ 5 characters from the f
'''

'''
## 讀取圖片，"rb" == "mode: read binary"
with open(photo, "rb") as p:
    print(p.read())
'''

'''
## Mode: a，會再原文的最後面，寫入新的文字
with open(path, "a") as f:
    f.write("###Hello, the 3rd\n")
    # print(f.read())             # You can't WRITE and READ at the same time

with open(path) as f:
    print(f.read())
'''

'''
## Mode: w，會將原文刪除，寫入新的文字
with open(path, "w") as f:
    f.write("#Where is the 1st line?\n")
    
with open(path) as f:
    print(f.read())
'''



import os    ## To delete a file, you must import the OS module, and run its os.remove() function:

'''
## 刪除檔案
if os.path.exists(photo):
    os.remove(photo)    
else:
    print("The file doesn't exist")
'''
  

## 只能刪除空的資料夾
if os.path.exists(subfolder):
    os.rmdir(subfolder)
    
else:
    print("The folder doesn't exist")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
