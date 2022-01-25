printableChars = [ chr(x) for x in range(ord('a'),ord('z')+1) ] # a-z, there is prob better/shortet list comprehension
print (printableChars) # just for testing purposes
 
def generateAllWords(length): 
    if length == 0: 
        yield '' 
    else: 
        for word in generateAllWords(length-1): # there should be a faster way to generate
            for char in printableChars: 
                yield ( word + char )

length = 6 # just for testing as well
for i in range(length):
    print(str(i)+':[ ', end='') # just to look nice 
    for word in generateAllWords(i):
        if (word!=''): # so there is no [ , ] for strings of len==0
            print(word,end=', ')
    print(']')
    
