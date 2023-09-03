#COLUMN TRANSPOSITION CIPHER
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
 
#ROW TRANSPOSITION CIPHER
def makeMatrixx(plainText, key):
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
           row.append('X')
       matrix.append(row)
   return matrix
def RowEncryption(plainText, key):
   matrix = makeMatrixx(plainText, key)
   sorted_key = ''.join(sorted(key))
   cipherText = []
   index = []
   for char in sorted_key:
       index.append(key.find(char))
   for row in matrix:
       for i in index:
           cipherText.append(row[i])
   return ''.join(cipherText)
def RowDecryption(cipherText, key):
   matrix = []
   row = []
   count = 0
   for char in cipherText:
       row.append(char)
       count += 1
       if count % len(key) == 0:
           matrix.append(row)
           row = []
   index = []
   sorted_key = ''.join(sorted(key))
   for char in key:
       index.append(sorted_key.find(char))
   plainText = []
   for row in matrix:
       for i in index:
           if row[i] != 'X':
               plainText.append(row[i])
   return ''.join(plainText)
 
#MAIN

while 1:
    print("\n===> MENU <===")
    print("\n(1)Encrypt & Decrypt using COLUMN transposition cipher")
    print("\n(2)Encrypt & Decrypt using ROW transposition cipher")
    print("\n(3)Exit")
    choice= input('\nEnter your choice: ')
    
    if(choice == '1'):
        plaintext = input('Enter the plaintext: ')
        keyword = input('Enter keyword: ')
        print('\nThe encrypted word is:',  ColumnEncryption(plaintext, keyword))
        ciphertext = input('Enter the ciphertext: ')
        decryptionkeyword = input('Enter keyword: ')
        print('Your Message is: ',ColumnDecryption(ciphertext, decryptionkeyword))
    
    elif (choice == '2'):
        plaintext = input('Enter the plaintext: ')
        keyword = input('Enter keyword: ')
        print('\nThe encrypted word is:',  RowEncryption(plaintext, keyword))
        ciphertext = input('Enter the ciphertext: ')
        decryptionkeyword = input('Enter keyword: ')
        print('Your Message is: ',RowDecryption(ciphertext, decryptionkeyword))
    
    else:
        break