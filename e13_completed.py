fileName = str(input("Δώστε το όνομα του αρχείου: "))
try:
    f = open(fileName, 'r')
    words = f.read().split()

    # Συνάρτηση για τον εντοπισμό της θέσης των λέξεων που το άθροισμα των γραμμάτων τους είναι 20
    def find_pair(li):
        for i in range( len(li)-1 ):
            for k in range(i, len(li)):
                if len( li[i]+li[k] ) == 20:
                    return (i, k)
        return (0,0)
    print("")
    while True:
        x = find_pair(words)
        if x != (0, 0):
            # Εκτυπώνεται το ζευγάρι των λέξεων
            print(words.pop(x[1]))
            print(words.pop(x[0]))
            print("")
        else:
            break

    # Η λίστα με τις λέξεις που έχουν απομείνει:
    print(words)
except:
    print("Δεν υπάρχει αρχείο με αυτό το όνομα. Σιγουρευτείτε ότι έχετε συμπεριλάβει και την κατάληξη .txt")
