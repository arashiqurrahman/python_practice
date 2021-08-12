#I want methods to encrypt and decrypt a Caesar Cipher message     
#Acceptance Criteria
#1.     Code written that can be followed
#2.     Encrypt and decrypt accept a message and a shift value as parameters
#3.     Letters from the message are rotated through the alphabet (a-z) by that number:
#1.	encrypt('hello', 1) =  'ifmmp'
#2.	decrypt('xpsme', 1) = 'world'

def encrypt(string, num):
    new_string = ""             
    for i in string:
        new_string+=chr(ord(i)+num)
    return new_string

print(encrypt('hello', 1))
    
def decrypt(string, num):
    new_string2 = "" 
    if type(string) is int:
        return "invalid"
    if string == "": 
        return "empty string"
    else:
        for i in string:
            if (ord(i)-num)<97:
                new_string2+=chr(ord(i)-num+26)
            else:
                new_string2+=chr(ord(i)-num)
            #print(ord(i))
        return new_string2

print(decrypt("ifmmp", 1))