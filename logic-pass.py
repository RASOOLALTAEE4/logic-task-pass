#Task1

#1- Remove Char from String

#Way 1

str = "hello every one1"
print ("Before Edit: ", str,"\nAfter Edit: ", str.replace("1", ""))

#Way 2 

def remChar(str, char):
    print ("After Edit:.... ",str.replace(char, ""))
    
st = input("Enter Text: ")
ch = input ("Enter Charcter: ")
remChar(st,ch)
    
    
#2- Find Prime Numbers    

Lower = 1
Upper = 10

for n in range (Lower,Upper+1):
    if n > 1:
        for i in range (2,n):
            if n % 2 == 0:
                break
            else:
                print ("The Prime Numbers are: ", n)

#3- Find Character Repeated

#Way 1
                
def repChar(x):
    
    for i in x:
        print("The Repeated Char: ",i,'is',x.count(i)) 
repChar(st)

#Way 2

my_string = "count a character occurance"
my_list = list(my_string)
for key in my_list:
    print (key, my_string.count(key))
