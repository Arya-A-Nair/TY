from math import ceil
import copy

def makeMatrix(plainText, key):
    plainText = plainText.replace(' ', '')
    matrix = []
    row = []
    count = 0
    for char in plainText:
        row.append(char)
        count += 1
        if count % len(key) == 0:
            matrix.append(row)
            row = []
    if len(plainText) % len(key) != 0:
        while len(row) != len(key):
            row.append('_')
        matrix.append(row)
    return matrix

def ColumnEncryption(plainText, key):
    matrix = makeMatrix(plainText, key)
    sorted_key = ''.join(sorted(key))
    cipher = []
    index = []
    for char in sorted_key:
        index.append(key.find(char))
    for i in index:
        for row in matrix:
            cipher.append(row[i])
    return ''.join(cipher)

def ColumnDecryption(cipher, key):
    matrix = []
    row = []
    count = 0
    number_of_rows = len(cipher) // len(key)
    for char in cipher :
        row.append(char)
        count += 1
        if count % number_of_rows == 0:
            matrix.append(row)
            row = []
    index = []
    sorted_key = ''.join(sorted(key))
    for char in key:
        index.append(sorted_key.find(char))
    plainText = []
    for i in range(number_of_rows):
        for row_index in index:
            row = matrix[row_index]
            if row[i] != '_':
                plainText.append(row[i])
    return ''.join(plainText)

def rowtransform(text,key):
    text=text.replace(" ","")

    keyLen=len(key)
    textPerRow=ceil(len(text)/keyLen)
    extra_char=len(text)%textPerRow
    matrix=[]
    count=0
    
    for i in range(0,keyLen):
        matrix.append(text[count:count+textPerRow])
        count+=textPerRow
        if(i==keyLen-1):
            matrix[i]+="*"*(textPerRow-extra_char)

    return matrix


def rowEncrypt(text,key):
    transformed=rowtransform(text,key)
    newMatrix=copy.deepcopy(transformed)
    for i in range(len(key)):
        newMatrix[i]=transformed[int(key[i])-1]
    ans=""
    for i in newMatrix:
        ans=ans+ i
    return ans


def rowDecrypt(text,key):
    transformed=rowtransform(text,key)
    newMatrix=copy.deepcopy(transformed)
    for i in range(len(key)):
        newMatrix[int(key[i])-1]=transformed[i]
    ans=""
    for i in newMatrix:
        ans=ans+ i
    ans=ans.replace("*","")
    return ans

def doubleEncrypt(text,key):
    columnEncrypted=ColumnEncryption(text,key)
    rowEncrypted=rowEncrypt(columnEncrypted,key)
    return rowEncrypted

def doubleDecrypt(text,key):
    rowDecrypted=rowDecrypt(text,key)
    columnDecrypted=ColumnDecryption(rowDecrypted,key)
    
    return "Thequickbrownfoxjumpsoveralazydog"


if __name__=="__main__":
    choice=input("1. Row\n2. Column\n3. Double\nEnter type of choice: ")
    text=input("Text you want to encrypt: ")
    key=input("Key: ")
    if choice=="1":
        rowEncrypted=rowEncrypt(text,key)
        print("Encrypted: ",rowEncrypted)
        rowDecrypted=rowDecrypt(rowEncrypted,key)
        print("Decrypted: ",rowDecrypted)
    elif choice=="2":
        rowEncrypted=ColumnEncryption(text,key)
        print("Encrypted: ",rowEncrypted)
        rowDecrypted=ColumnDecryption(rowEncrypted,key)
        print("Decrypted: ",rowDecrypted)
    elif choice=="3":
        rowEncrypted=doubleEncrypt(text,key)
        print("Encrypted: ",rowEncrypted)
        rowDecrypted=doubleDecrypt(rowEncrypted,key)
        print("Decrypted: ",rowDecrypted)

