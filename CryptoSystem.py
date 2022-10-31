# "asciiList" : contains all the chars wich can be found in keyboard (except chars that can't be used in a password) BUT, careful!!! "TAB" character is not in "asciiList", 
# so if some password contains "TAB" then "Encryptor"/"Decryptor" functions will NOT WORK!!!

asciiList = [   " ", "!", "\"", "#", "$", "%", "&", "\'", "(", ")",
                "*", "+", ",", "-", ".", "/", "0", "1", "2", "3",
                "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", 
                ">", "?", "@", "A", "B", "C", "D", "E", "F","G", 
                "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", 
                "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[",
                "\\", "]", "^", "_", "`", "a", "b", "c", "d","e", 
                "f", "g", "h", "i", "j","k", "l", "m", "n", "o",
                "p","q", "r", "s", "t", "u", "v","w", "x", "y",
                "z", "{", "|", "}", "~"                             ]

listSize = len(asciiList)   # "listSize" contains how many chars are in asciiList

# "Encryptor" function takes the password we want to encrypt(password : type = str), and the key that will help us(key : type = str)
def Encryptor(password, key) :
    keyIndexesList = []         # "keyIndexesList" : will contain the indexes of every char of key (based on asciiList)
    passwordIndexesList = []    # "passwordIndexesList" : will contain the indexes of every char of password (based on asciiList)
    encrypted = ""              # "encrypted" : at the end of that function (if everything works fine) will contain the final encrypted password

    for i in range(len(key)) :                          # At the end of that for, "keyIndexesList" will contains the indexes of every char of "key"
        for j in range(len(asciiList)) :
            if (key[i] == asciiList[j]) :
                keyIndexesList.append(j)

    for i in range(len(password)) :                     # At the end of that for, "passwordIndexesList" will contains the indexes of every char of "password"
        for j in range(len(asciiList)) :
            if (password[i] == asciiList[j]) :
                passwordIndexesList.append(j)

    j = 0
    for i in range(len(password)) :                                                 # That for is doing all the work, we sub every index of "passwordIndexesList"
        if (j == len(key)) : j = 0                                                  # with the index of keyIndexesList (in case result < 0, we sub the negative result with last index in "asciiList").
        if (passwordIndexesList[i] - keyIndexesList[j] < 0) :                       # Now if length of key is < than length of password, everytime index "j"(who shows at "key") is equals with length of key,
            movedIndex = listSize - (keyIndexesList[j] - passwordIndexesList[i])    # we "send" it at the start (index "j" = 0), looks like a loop.
        else :                                                                      # So finally we have a different password at valable "encrypted"
            movedIndex = passwordIndexesList[i] - keyIndexesList[j]
        encrypted += asciiList[movedIndex]
        j += 1

    return encrypted

# "Decryptor" function looks pretty much like "Encryptor" function, again with a "password" and "key" for inputs, BUT careful!!!,
# the "key" must be exactly the same with the "key" that entered in "Encryptor" function AND the "password" must be exactly 
# the same with the encrypted "password" which returned from "Encryptor" function, otherwise decryption won't work correcty, 
# and the original code will never be found.
def Decryptor(password, key) :
    keyIndexesList = []
    passwordIndexesList = []
    decrypted = ""

    for i in range(len(key)) :                      # # At the end of that for, "keyIndexesList" will contains the indexes of every char of "key"
        for j in range(len(asciiList)) :
            if (key[i] == asciiList[j]) :
                keyIndexesList.append(j)

    for i in range(len(password)) :                 # At the end of that for, "passwordIndexesList" will contains the indexes of every char of "password"
        for j in range(len(asciiList)) :
            if (password[i] == asciiList[j]) :
                passwordIndexesList.append(j)

    j = 0
    for i in range(len(password)) :                                                 # That "for" do same job with last "for" in "Encryptor" function
        if (j == len(key)) : j = 0                                                  # except that it doesn't sub the indexs, but it adds them (kinda like the reverse job of "Encryptor" func.)
        if (passwordIndexesList[i] + keyIndexesList[j] >= listSize) :               # so at the end of "Decryptor" function, if everything work fine, 
            movedIndex = (passwordIndexesList[i] + keyIndexesList[j]) - listSize    # the prototype (decrypted) password will be in "decrypted" variable
        else :
            movedIndex = passwordIndexesList[i] + keyIndexesList[j]
        decrypted += asciiList[movedIndex]
        j += 1

    return decrypted

# Menu
print("#################################")
print("#    Welcome to CryptoSystem    #")
print("#################################")

cont = 1
while (cont == 1) :
    print()
    print("Press 1 if you want to Encrypt a password.")
    print("Press 2 if you want to Decrypt a password.")
    choise = int(input())

    if (choise == 1) :
        print()
        password = input("Give the password you want to encrypt           : ")
        key = input("Give the key (encryption will be based on that) : ")
        encrypted = "\""                                                        # We start and end the password with "
        encrypted += Encryptor(password, key)                                   # just to be clear the chars of our password
        encrypted += "\""                                                       # in case that password has space(s)
        print()
        print("The new Encrypted password is : \n")
        print(encrypted, "and its length is :", len(encrypted) - 2)

    if (choise == 2) :
        print()
        password = input("Give the password you want to decrypt           : ")
        key = input("Give the key (decryption will be based on that) : ")
        decrypted = "\""
        decrypted += Decryptor(password, key)
        decrypted += "\""
        print()
        print("The decrypted password is : \n")
        print(decrypted, "and its length is :", len(decrypted) - 2)

    print()
    cont = int(input("If you want to continue, press 1 : "))
