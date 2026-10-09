

# check positive / negative number

def is_positive(n):
    return "positive" if n > 0 else "non positive"

n = float(input("Insert number: "))
print(is_positive(n))