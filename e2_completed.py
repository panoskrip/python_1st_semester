import random

n = int(input("Δώστε τον όρο της Aκολουθίας Fibonacci που θέλετε να δείτε αν είναι πρώτος ή οχι: "))

def fib(n):
    #Γρήγορη συνάρτηση για τον υπολογισμό του n όρου της Ακολουθίας Fibonacci
    v1, v2, v3 = 1, 1, 0    #initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  #perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
        
    #20 τυχαίες δοκιμές
    count = 0
    for i in range(20):
        a = random.randint(1,100)
        if (a**v2) % v2 == a % v2:
            count += 1  
         
    if count == 20:
        print("Ο", n, "ος όρος της Ακολουθίας Fibonacci, δηλαδή ο αριθμός", v2, "είναι πρώτος.")
    else:
        print("Ο", n, "ος όρος της Ακολουθίας Fibonacci, δηλαδή ο αριθμός", v2, "δεν είναι πρώτος.")

fib(n)