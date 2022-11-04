#Backend people: write this iteratively.
#Frontend people: write this recursively.
def factorial(n):
  if n==0:
    return 1
  else:
    return n*factorial(n-1)

#Everyone, make the print statement print your name.
def printName():
  print("Bryan")

if __name__ == "__main__":
  print(factorial(5))
  printName()

