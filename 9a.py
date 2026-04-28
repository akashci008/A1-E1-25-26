fav = int(input("Enter number of favorable outcomes: "))
total = int(input("Enter total number of outcomes: "))

if total == 0:
    print("Total outcomes cannot be zero")
else:
    probability = fav / total
    print("P(A) =", probability)