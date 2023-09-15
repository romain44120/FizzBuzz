def fizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

# Demande à l'utilisateur d'entrer un nombre
num = int(input("Entrez un nombre entier : "))
result = fizzBuzz(num)
print("Résultat de FizzBuzz pour", num, ":", result)