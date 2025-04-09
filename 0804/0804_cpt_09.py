# Chiediall'utente di inserire un numero N. Il programma dovrebe stampare la sequenza di Fibonacci fino a N. 

# Ad esempio, se l'utente inserisce 100, il programma dovrebbe stampare tutti i numeri della sequenza di Fibonacci minori o uguali a 100.

def fibonacci(n):
    a,b = 0, 1
    sequenza =[]
    
    while a <= n:
        sequenza.append(a)
        a,b =b, a + b
    return sequenza

n = int((input("Dimmi un numero")))

sequenza = fibonacci(n)

print("La sequenza di Fibonacci fino a tuo numero", n, "è", sequenza)






