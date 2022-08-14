#Remove Char from String

#Way 1

str = "hello every one1"
print ("Before Edit: ", str,"\nAfter Edit: ", str.replace("1", ""))

#Way 2 

def remChar(str, char):
    print ("After Edit:.... ",str.replace(char, ""))
    
st = input("Enter Text: ")
ch = input ("Enter Charcter: ")
remChar(st,ch)
    
    
#Find Prime Numbers    

Lower = 1
Upper = 10
prime = []
for n in range (Lower,Upper+1):
    if n > 1:
        for i in range (2,n):
            if n % 2 == 0:
                break
            else:
                print ("The Prime Numbers are: ", n)
