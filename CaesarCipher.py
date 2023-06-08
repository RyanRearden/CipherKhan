cipher = input('Please input a cipher:\n')

#Easier than navigating upper and lower case ASCII
cipher = cipher.upper()

charList = []

#Keeps spaces, otherwise creates a list of numbers where A = 0 and Z = 25
for chars in cipher: 
    if (ord(chars) != 32):
        charList.append((ord(chars))- 65)
    else:
        charList.append(ord(chars))
    print(charList)
y = 0

#All shifts plus the original are looped
while y < 26:
    
    #creates a new list with a shift of + 1 every time (but loops so 25+1 becomes 1)
    #if it is the ASCII value of 32 ('space') then it leaves it
    charList = list(map(lambda x: x if(x == 32)  else (x + 1)%26, charList))

    #Turns decimal value into char 
    #Adds 65 because A is 65 in ASCII
    charVals = list(map(lambda x: chr(x) if(x == 32) else(chr(x + 65)), charList))

    #Taken from GeeksForGeeks -- looked like a short way to do it 
    listToStr = ''.join([str(elm) for elm in charVals])


    print(listToStr)
    print()
    y = y + 1





    

