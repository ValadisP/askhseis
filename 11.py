f=open("mytxt.txt","r")
#Εισαγει ο χρηστης μια 6αδα αριθμων και 
#φτιαχνω μια λιστα με τους αριθμους αυτους 
#με τον καθενα ξεχωριστα
six=input()
b=[str(i) for i in str(six)]
print (b)
#Χωριζω τις τετραδες 
fours=f.read()
fours=fours.split()
#Ελεγχω για καθε τετραδα αν υπαρχουν οι δοσμενοι αριθμοι 
for line in fours:
    crrct=0
    for i in list(b):
         if i in line:
            crrct+=1
    if crrct>=4 :
        print("Υπαρχει")
        break
if crrct<4 :
    print ("Δεν υπαρχει")




    

