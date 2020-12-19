fileName = str(input("Δώστε το όνομα του αρχείου: "))

f = open(fileName, 'r')

words = f.read().split()

def find_pair(l):
    for i in range(len(l)-1):
        for k in range(i, len(l)):
            if len(l[i]+l[k])==20:
                return (i, k)
    return (0,0)

while True:
    x=find_pair(words)
    if x!=(0,0):
        print(words.pop(x[1]))
        print(words.pop(x[0]))
        print("")
    else:
        break

print(words)
