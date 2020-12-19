fileName = str(input("Δώστε το όνομα του αρχείου: "))
f = open(fileName, 'r')
try:
    #Δημιουργία λίστας, με κάθε στοιχείο να είναι και μία λέξη
    words = f.read().split()
    #Δημιουργία λίστας με κάθε στοιχείο να είναι και ένα γράμμα
    letters = []
    for word in words:
        for letter in word:
            letters.append(letter)
        #Στο τέλος κάθε λέξη τοποθετείται και ένα κενό
        letters.append("")
    
    #Δημιουργία λίστας με κάθε στοιχείο να είναι ο αριθμός ASCII       
    asciiList = []
    for letter in letters:
        try:
            asciiList.append(255 - ord(letter)) 
        except:
            #Σε περίπωση που το στοιχείο της λίστας letters είναι το κενό, γίνεται append ο αριθμός 32, που είναι ο κωδικός ASCII για το SPACE
            asciiList.append(32)
    
    #Η λίστα αντιστρέφεται    
    asciiList.reverse()

    #Η λίστα με τους αριθμούς ASCII μετατρέπεται ξανά σε χαρακτήρες
    final = []
    for num in asciiList:
        final.append(chr(num))
     
    #Τυπώνεται κάθε γράμμα ξεχωριστά   
    for letter in final:
        print(letter)
except:
    print("Δεν υπάρχει αρχείο με αυτό το όνομα. Σιγουρευτείτε ότι έχετε συμπεριλάβει και την κατάληξη .txt")
