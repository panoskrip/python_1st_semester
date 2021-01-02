import random

#Ο χρήστης εισάγει την διάσταση του τετραγώνου
dimension = int(input("Δώστε την διάσταση του τετραγώνου: "))

count = 0

#Δημιουργία των λιστών
#Μέσα στην mainList βρίσκονται dimension αριθμός στοιχείων, με κάθε στοιχείο να περιέχει μία λίστα με dimension αριθμό στοιχείων
mainList = []
insideList = []
for i in range(dimension):
    insideList.append(" ")

for i in range(dimension):
    mainList.append(insideList[:])

#Τυχαία εισαγωγή S ή O

sLeft = int((dimension*dimension)/2) #sLeft = πόσα S είναι διαθέσιμα να μπουν
oLeft = int((dimension*dimension)/2) #Ομοίως

for i in range(100):
    #Αν το τετράγωνο έχει μονό αριθμό στοιχείων, τότε διαλέγεται τυχαία ένα περισσότερο S ή O
    if (dimension*dimension) % 2 == 1:
        temp = random.randint(1,2)
        if temp == 1:
            sLeft += 1
        else:
            oLeft += 1

    #Τα S και O μπαίνουν στο τετράγωνο
    for i in range(dimension):
        tempList = mainList[i]
        for j in range(dimension):
            temp = random.randint(1,2)
            if temp == 1:
                if sLeft > 0:
                    tempList[j] = "S"
                    sLeft -= 1
                else:
                    tempList[j] = "O"
            else:
                if oLeft > 0:
                    tempList[j] = "O"
                    oLeft -= 1
                else:
                    tempList[j] = "S"
        mainList[i] = tempList

    # for i in range(dimension):
    #     print(mainList[i])

    #Οριζόντια
    for i in range(dimension):
        for j in range(dimension-2):
            if mainList[i][j] == 'S' and mainList[i][j+1] == 'O' and mainList[i][j+2] == 'S':
                count += 1

    #Κάθετα
    for j in range(dimension):
        for i in range(dimension-2):
            if mainList[i][j] == "S" and mainList[i+1][j] == "O" and mainList[i+2][j] == "S":
                count +=1

    #Διαγώνια (από πάνω αριστερά σε κάτω δεξιά)
    #(πάνω μισό)

    for k in range(dimension):
        j = 0
        temporaryList = []
        while j <= k:
            i = k - j
            if k>=2:
                temporaryList.append(mainList[i][j])
            j += 1
        if k>=2:
            liLenght = len(temporaryList)
            for v in range(liLenght-2):
                if temporaryList[v] == "S" and temporaryList[v+1] == "O" and temporaryList[v+2] == "S":
                    count += 1
    
    #(κάτω μισό)
    k = dimension - 2
    while k >= 0:
        j = 0
        temporaryList2 = []
        while j <= k:
            i = k - j
            if k>=2:
                temporaryList2.append(mainList[dimension-j-1][dimension-i-1])
                
            j += 1
        if k>=2:
            liLenght = len(temporaryList2)
            for v in range(liLenght-2):
                if temporaryList2[v] == "S" and temporaryList2[v+1] == "O" and temporaryList2[v+2] == "S":
                    count += 1 
        k -= 1

    # Η κάθε σειρά του πίνακα αντιστρέφεται για να γίνει ο έλεγχος της διαγωνίου από πάνω δεξία προς κάτω αριστερά 
    # με τον ίδιο αλγόριθμο που έγινε και από πάνω αριστερά προς κάτω δεξιά
    for i in range(dimension):
        mainList[i].reverse()
        
    #(πάνω μισό)
    for k in range(dimension):
        j = 0
        temporaryList = []
        while j <= k:
            i = k - j
            if k>=2:
                temporaryList.append(mainList[i][j])
            j += 1
        if k>=2:
            liLenght = len(temporaryList)
            for v in range(liLenght-2):
                if temporaryList[v] == "S" and temporaryList[v+1] == "O" and temporaryList[v+2] == "S":
                    count += 1
    
    #(κάτω μισό)
    k = dimension - 2
    while k >= 0:
        j = 0
        temporaryList2 = []
        while j <= k:
            i = k - j
            if k>=2:
                temporaryList2.append(mainList[dimension-j-1][dimension-i-1])
                
            j += 1
        if k>=2:
            liLenght = len(temporaryList2)
            for v in range(liLenght-2):
                if temporaryList2[v] == "S" and temporaryList2[v+1] == "O" and temporaryList2[v+2] == "S":
                    count += 1 
        k -= 1

print(count/100)
