f=open("mytxt.txt","r")
lex=[]
a="EIUAO"
a+=a.lower()
#Φτιαχω μια λιστα με ολες τις λεξεις και στη συνεχεια παιρνω καθε λεξη μονο μια φορα
for line in f:
    lex+=line.split()
lex=list(set(lex))
#Φτιαχνω μια λιστα που περιεχει τις reversed λεξεις και τις ταξινομω 
finalf = [ wrd[::-1] for wrd in lex ]
finalf.sort(reverse=True)
#Παιρω τις πρωτες 5 λεξεις και τις βγαζω τα φωνηεντα 
b = finalf[:5]
for wrd in b:
    newf=wrd
    for letter in wrd: 
        if letter in list(a):
            newf = newf.replace(letter,"")
    print (newf)

  





